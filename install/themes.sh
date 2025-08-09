#!/bin/bash

# Getting path from arguments
BASE_DIR="$1"

echo "Downloading themes..."
yay -S --needed --noconfirm arc-gtk-theme

#gsettings set org.gnome.desktop.interface gtk-theme "Arc-Dark"

echo "Downloading fonts.."
sudo pacman -S --needed --noconfirm ttf-jetbrains-mono ttf-nerd-fonts-symbols

echo "Setting wallpaper"
cp $BASE_DIR/data/wallpaper ~/Pictures