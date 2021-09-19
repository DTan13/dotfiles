import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401
from libqtile.widget import backlight

# WM Name
wmname = "qtile"
# my short name keys
SUPER = "mod4"
ALT = "mod1"
CTRL = "control"
PRT_SC = "Print"
fnUP = "XF86AudioRaiseVolume"
fnDOWN = "XF86AudioLowerVolume"
fnVoff = "XF86AudioMute"
RET = "Return"
SPC = "space"
# My short name apps
TERM = "alacritty"
EDITOR = "nvim"
BRS = "brave"
FileManager = "pcmanfm"

keys = [
    # Switch window focus to other pane(s) of stack
    Key([ALT], "Tab", lazy.layout.next()),

    # RESIZE UP, DOWN, LEFT, RIGHT
    Key([SUPER, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([SUPER, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([SUPER, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([SUPER, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([SUPER, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([SUPER, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([SUPER, "shift"], "Left", lazy.layout.swap_left()),
    Key([SUPER, "shift"], "Right", lazy.layout.swap_right()),

    # TOGGLE FLOATING LAYOUT
    Key([SUPER, "shift"], "space", lazy.window.toggle_floating()),

    Key([SUPER], "n", lazy.next_layout()),
    
    # Swap panes of split stack
    Key([SUPER, "shift"], SPC, lazy.layout.rotate()),
    
    # multiple stack panes
    Key([SUPER, "shift"], RET, lazy.layout.toggle_split()),
    
    # Screen Shot with scrot
    Key([], PRT_SC, lazy.spawn("bash -c \"cd ~/Pictures/Screenshots/qtile;scrot\"")),
    
    # applications shortcat
    Key([SUPER], RET, lazy.spawn(TERM)),
    Key([SUPER], "f", lazy.spawn(BRS)),
    Key([SUPER], "e", lazy.spawn(FileManager)),
    Key([SUPER], "t", lazy.spawn("kotatogram-desktop")),
    
    Key([SUPER], "Tab", lazy.screen.next_group(skip_empty=True)),
    Key([SUPER,"shift"], "Tab", lazy.screen.prev_group()),

    Key([SUPER], "w", lazy.window.kill()),
    Key([SUPER, CTRL], "r", lazy.restart()),
    Key([SUPER, CTRL], "q", lazy.shutdown()),
    Key([SUPER],"m",lazy.window.cmd_toggle_maximize()),

    # INCREASE/DECREASE/MUTE VOLUME
    Key([], fnUP, lazy.spawn("amixer -q set Master 5%+")),
    Key([], fnDOWN, lazy.spawn("amixer -q set Master 5%-")),
    Key([], fnVoff, lazy.spawn("amixer -q set Master toggle")),

    # INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-")),

    # dmenu Run
    Key([SUPER], "d", lazy.spawn(" dmenu_run -fn 'Source Code Pro Semibold:size=13' -nb '#282a36' -nf '#fefefe' ")),
    
    # locking
    Key([SUPER], "l",lazy.spawn("lxlock")),
    Key([SUPER],"Delete",lazy.spawn("systemctl suspend")),
    ]

# GROUPS

groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.append(
        Key([SUPER], str(i.name), lazy.group[i.name].toscreen())
    )  # Switch to another group
    keys.append(
        Key([SUPER, "shift"], str(i.name), lazy.window.togroup(i.name))
    )  # Send current window to another group

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {
    "border_width": 1,
    "margin": 0,
    "border_focus": "e1acff",
    "border_normal": "1D2330",
}

##### THE LAYOUTS #####
layouts = [
    layout.Max(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Floating(**layout_theme),
    #  layout.Bsp(**layout_theme),
    #  layout.MonadWide(**layout_theme),
    #  layout.Stack(stacks=2, **layout_theme),
    #  layout.Columns(**layout_theme),
    #  layout.VerticalTile(**layout_theme),
    #  layout.Matrix(**layout_theme),
    #  layout.Zoomy(**layout_theme),
    #  layout.Tile(shift_windows=True, **layout_theme),
]

##### COLORS #####
colors = [
    ["#282a36", "#282a36"],  # panel background
    ["#24262F", "#24262F"],  # background for current screen tab
    ["#ffffff", "#ffffff"],  # font color for group names
    ["#BD93F9", "#BD93F9"],  # border line color for current tab
    ["#8d62a9", "#8d62a9"],  # border line color for other tab and odd widgets
    ["#44475A", "#44475A"],  # color for the even widgets
    ["#e1acff", "#e1acff"],  # window name
]

##### PROMPT #####
# prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(font="Source Code Pro Medium", fontsize=16, padding=4)
extension_defaults = widget_defaults.copy()

##### WIDGETS #####
def init_widgets_list():
    widgets_list = [
        widget.CurrentLayoutIcon(scale=0.75),
        widget.Sep(linewidth=0, padding=5,
                   foreground=colors[2], background=colors[0]),
        widget.GroupBox(disable_drag=True,highlight_method="block", inactive="999999"),
        widget.Sep(linewidth=0, padding=5,
                   foreground=colors[2], background=colors[0]),
        widget.WindowName(format='{name}',max_chars=60),
        widget.Notify(),
        widget.CPU(format='{freq_current}GHz {load_percent}%',
                    foreground=colors[2], background=colors[0]),
        widget.Memory(format='{MemUsed: .0f}{mm}/{MemTotal:.0f}{mm}',
                    foreground=colors[2], background=colors[0]),
        widget.Sep(linewidth=0, padding=4,
                   foreground=colors[2], background=colors[0]),
        widget.Net(format='{down} ↓↑ {up}',foreground=colors[2],background=colors[0]),
        widget.Sep(linewidth=0,padding=4,
                    foreground=colors[2],background=colors[0]),
        widget.TextBox(text=" Vol:", padding=1 ),
        widget.Volume(padding=5),
        widget.Sep(linewidth=0, padding=4,
                   foreground=colors[2], background=colors[0]),
        widget.Battery(energy_now_file = "charge_now",
                                energy_full_file = "charge_full",
                                power_now_file = "current_now",
                                update_delay = 1,
                                foreground = colors[2],
                                charge_char = u'↑',
                                discharge_char = u'↓',),
        widget.Sep(linewidth=0, padding=4,
                   foreground=colors[2], background=colors[0]),
        widget.Backlight(backlight_name="intel_backlight", change_command=None, step=1),
        widget.Systray(),
        widget.Sep(linewidth=0, padding=4,
                   foreground=colors[2], background=colors[0]),
        widget.Clock(format="%A %d %B %H:%M"),
        widget.Sep(linewidth=0, padding=4,
                   foreground=colors[2], background=colors[0]),
    ]
    return widgets_list


# SCREENS ##### (TRIPLE MONITOR SETUP)

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1  # Slicing removes unwanted widgets on Monitors 1,3


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2  # Monitor 2 will display all widgets in widgets_list


def init_screens():
    return [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen1(),
                size=24,
                background=['#282a36'],
                opacity=0.8
            )
        ),
        Screen(
            bottom=bar.Bar(
                widgets=init_widgets_screen2(),
                size=24,
                background=["#282a36"],
                opacity=0.8
            )
        ),
    ]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    #  widgets_screen1 = init_widgets_screen1()
    #  widgets_screen2 = init_widgets_screen2()

##### DRAG FLOATING WINDOWS #####
mouse = [
    Drag(
        [SUPER],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [SUPER],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click([SUPER], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

##### FLOATING WINDOWS #####
#  floating_layout = layout.Floating(
#      float_rules=[
#          {"wmclass": "confirm"},
#          {"wmclass": "dialog"},
#          {"wmclass": "download"},
#          {"wmclass": "error"},
#          {"wmclass": "file_progress"},
#          {"wmclass": "notification"},
#          {"wmclass": "splash"},
#          {"wmclass": "toolbar"},
#          {"wmclass": "confirmreset"},  # gitk
#          {"wmclass": "makebranch"},  # gitk
#          {"wmclass": "maketag"},  # gitk
#          {"wname": "branchdialog"},  # gitk
#          {"wname": "pinentry"},  # GPG key password entry
#          {"wmclass": "ssh-askpass"},  # ssh-askpass
#      ]
#  )
auto_fullscreen = True
focus_on_window_activation = "smart"

##### STARTUP APPLICATIONS #####

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
