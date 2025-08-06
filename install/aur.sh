#!/bin/bash

if ! command -v yay &>/dev/null; then
    echo "Installing yay"
    git clone https://aur.archlinux.org/yay.git
    cd yay
    touch testfile.txt
    cd ..
else
    echo "yay already installed!!"
fi