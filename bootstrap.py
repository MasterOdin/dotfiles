#!/usr/bin/env python
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
HOME_DIR = os.path.expanduser("~")

# SETUP BREW
os.system("./brew.py")

# SETUP ZSH
os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')

zsh_cp = os.path.join(CURRENT_DIR, "zsh", ".zshrc")
zsh_dest = os.path.join(HOME_DIR, ".zshrc")
os.system("cp {} {}".format(zsh_cp, zsh_dest))

theme_cp = os.path.join(CURRENT_DIR, "zsh", "duellj-custom.zsh-theme")
theme_dist = os.path.join(HOME_DIR, ".oh-my-zsh", "themes", "duellj-custom.zsh-theme")
os.system("cp {} {}".format(theme_cp, theme_dist))
