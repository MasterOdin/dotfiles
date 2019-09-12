#!/usr/bin/env bash

if [[ "${OSTYPE}" == "darwin"* ]]; then
    source bootstrap/macOS.sh
fi

# other values for ${OSTYPE}:
#   linux-gnu
#   cygwin
#   msys
#   win32
#   "freebsd"*
