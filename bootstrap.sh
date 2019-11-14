#!/usr/bin/env bash

THIS_DIR="$( cd "$(dirname "$0")" ; pwd -P )"

__green="\033[32m"
__red="\033[31m"
__gray="\033[1;30m"
__blue="\033[34m"
__magenta="\033[35m"
__reset="\033[0m"

# Install dependencies
case "$(uname)" in
"Darwin")
    source ${THIS_DIR}/scripts/macOS.sh
;;

"Linux")
    >&2 echo "Linux not yet supported"
;;
esac

# other values for ${OSTYPE}:
#   linux-gnu
#   cygwin
#   msys
#   win32
#   "freebsd"*

# Install oh-my-zsh
if [ -d ${HOME}/.oh-my-zsh ]; then
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
fi

ZSH_CUSTOM=${HOME}/.oh-my-zsh/custom

# Add some ZSH plugins
if [ ! -d ${ZSH_CUSTOM}/plugins/zsh-syntax-highlighting ]; then
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM}/plugins/zsh-syntax-highlighting
else
    pushd ${ZSH_CUSTOM}/plugins/zsh-syntax-highlighting
    git pull
    popd
fi

# Source things
rm -f ${HOME}/.zshrc
ln -s ${THIS_DIR}/.zshrc ${HOME}/.zshrc
rm -f ${HOME}/.oh-my-zsh/custom/themes/honukai.zsh-theme
ln -s ${THIS_DIR}/oh-my-zsh/custom/themes/honukai.zsh-theme ${HOME}/.oh-my-zsh/custom/themes/honukai.zsh-theme

source ${HOME}/.zshrc
