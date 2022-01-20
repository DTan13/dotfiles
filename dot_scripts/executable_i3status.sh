#!/bin/bash

# Auto detect interfaces
ifaces=$(ls /sys/class/net | grep -E '^(eno|enp|ens|enx|eth|wlan|wlp)')

last_time=0
last_rx=0
last_tx=0
rate=""

readable() {
  local bytes=$1
  local kib=$((bytes >> 10))
  if [ $kib -lt 0 ]; then
    echo "? K"
  elif [ $kib -gt 1024 ]; then
    local mib_int=$((kib >> 10))
    local mib_dec=$((kib % 1024 * 976 / 10000))
    if [ "$mib_dec" -lt 10 ]; then
      mib_dec="0${mib_dec}"
    fi
    echo "${mib_int}.${mib_dec} M"
  else
    echo "${kib} K"
  fi
}

update_rate() {
  local time=$(date +%s)
  local rx=0 tx=0 tmp_rx tmp_tx

  for iface in $ifaces; do
    read tmp_rx <"/sys/class/net/${iface}/statistics/rx_bytes"
    read tmp_tx <"/sys/class/net/${iface}/statistics/tx_bytes"
    rx=$((rx + tmp_rx))
    tx=$((tx + tmp_tx))
  done

  local interval=$(($time - $last_time))
  if [ $interval -gt 0 ]; then
    rate="$(readable $(((rx - last_rx) / interval))) ↓ $(readable $(((tx - last_tx) / interval))) ↑"
  else
    rate=""
  fi

  last_time=$time
  last_rx=$rx
  last_tx=$tx
}

i3status | (read line && echo "$line" && read line && echo "$line" && read line && echo "$line" && update_rate && while :; do
  read line
  # for net-speed
  update_rate
  # for window name
  id=$(xprop -root | awk '/_NET_ACTIVE_WINDOW\(WINDOW\)/{print $NF}')
  name=$(xprop -id $id | awk '/_NET_WM_NAME/{$1=$2="";print}' | cut -d'"' -f2)
  name=${name//\\/\\\\}
  name=${name//\"/\\\"}

  # MPC current Song
  MAX_LENGTH="40"
  INFO="$(mpc status)"
  SONG="$(mpc current)"
  NAME_LENGTH="${#SONG}"
  if [ "$NAME_LENGTH" -gt "$MAX_LENGTH" ]; then
    SONG="${SONG:0:$MAX_LENGTH}"
    SONG=" | $SONG…"
  fi
  STATE="$(echo $INFO | head -n 2)"

  # This is working so
  echo ",[{\"full_text\":\"$name${SONG} | ${rate}\" },${line#,\[}" || exit 1
done)
