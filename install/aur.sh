#!/bin/bash

if ! command -v yay &>/dev/null; then
    echo "Installing yay"
    git clone https://aur.archlinux.org/yay.git
    cd yay/
    sudo makepkg -si --noconfirm
    cd ..
    rm -rf yay
else
    echo "AUR helper (yay) already installed!!"
fi
