#!/bin/bash

# Getting path from arguments
BASE_DIR="$1"
echo "dir: $BASE_DIR/data/lightdm"

if ! command -v lightdm &>/dev/null; then
    echo "Installing display manager"
    yay -S --needed --noconfirm lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings
else
    echo "Display manager (lightdm) already installed!!"
fi

# lightdm-gtk-greeter configuration
sudo cp -f $BASE_DIR/data/lightdm/lightdm-gtk-greeter.conf /etc/lightdm/lightdm-gtk-greeter.conf

# Setting lightdm background image  
sudo cp -f $BASE_DIR/data/lightdm/login-background.jpg /usr/share/backgrounds/login-background.jpg

# Starting lightdm service
sudo systemctl enable lightdm