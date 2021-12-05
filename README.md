# DTan13's dotfiles

## Installation

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/DTan13/dotfiles/main/setup)"
```

This script assumes you have either `apt` , `pacman` or `yum` installed on your system.

### Defaults
- CLI
	- `zsh`
	- `vim`
	- `tmux`
	- `gitui`
	- `gdb`
	- `tty`
	- `fzf`
	- `amfora`
- GUI
	- `qtile`
	- `i3`
	- `alacritty`
	- `zathura`


#### Tips
- If after installing `oh-my-zsh`, you are stuck in `zsh`. Just `exit`.
- While running `nvim` for the first time you have to run `:PlugUpdate` or `:PlugInstall` to fetch all plugins.
- Same for `tmux` , to fetch plugins use `<prefix>`+`I`.
