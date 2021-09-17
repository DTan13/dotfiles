# DTan13's dotfiles

## Installation

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/DTan13/dotfiles/main/setup)"
```

This script assumes you have either `apt` , `pacman` or `yum` installed on your system.

### Defaults 
> for now
- CLI
	- `zsh`
	- `neovim`
	- `tmux`
	- `gitui`
- GUI
	- `qtile`
	- `alacritty`
	- `zathura`


#### Tips
- After installing `oh-my-zsh` you are stuck in terminal. Just `exit`
- While running `nvim` for the first time you have to run `:PlugUpdate` or `:PlugInstall` to fetch all plugins
- Same for `tmux` , to fetch flugins use `<prefix>`+`I`
