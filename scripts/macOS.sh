#!/usr/bin/env bash

# Install Homebrew (https://brew.sh)
if [ ! $(command -v brew) ]; then
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

brew install python node ffmpeg nano thefuck ruby git wget
