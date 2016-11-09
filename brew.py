#!/usr/bin/env python
import os

os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
os.system("brew update")
os.system("brew upgrade")

# I forget what taps come standard with brew
taps = [
"caskroom/cask",
"caskroom/versions",
"cloudfoundry/tap",
"homebrew/apache",
"homebrew/boneyard",
"homebrew/core",
"homebrew/dupes",
"homebrew/php",
"homebrew/science",
"homebrew/services",
"homebrew/versions",
]

packages = [
"asciidoc",
"autoconf",
"automake",
"berkeley-db4",
"cf-cli",
"cmake",
"composer",
"curl",
"docbook",
"eigen",
"erlang",
"ffmpeg",
"freetype",
"gcc",
"geckodriver",
"go",
"gradle",
"graphviz",
"httpd24",
"hub",
"imagemagick",
"lastpass-cli",
"libpng",
"mongodb",
"mysql",
"node",
"openssl",
"perl",
"phantomjs",
"php70",
"php70-xdebug",
"pkg-config",
"postgresql",
"python",
"python3",
"rabbitmq",
"ruby",
"thefuck",
"wget",
"yarn",
"zeromq",
"zlib",
"zsh",
"zsh-completions"
]

for tap in taps:
    os.system("brew tap {}".format(tap))

os.system("brew install {}".format(" ".join(packages)))

os.system("brew cleanup")
os.system("brew doctor")
