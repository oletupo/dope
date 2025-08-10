#!/bin/bash

echo "Installing base applications..."

# X11
sudo pacman -S --needed --noconfirm xorg xf86-video-fbdev

# Wayland
#sudo pacman -S --needed --noconfirm wlroots pywlroots xorg-xwayland

# Network
sudo pacman -S --needed --noconfirm wpa_supplicant networkmanager network-manager-applet

# Audio
sudo pacman -S --needed --noconfirm pipewire alsa-utils pavucontrol

# Desktop environment base apps
sudo pacman -S --needed --noconfirm qtile picom rofi dunst polkit polkit-gnome

# Terminals
sudo pacman -S --needed --noconfirm ghostty alacritty xfce4-terminal

# Text editors
sudo pacman -S --needed --noconfirm neovim geany

# Web browser
sudo pacman -S --needed --noconfirm firefox

# File management
sudo pacman -S --needed --noconfirm thunar ranger thunar-volman udiskie ntfs-3g fuse gvfs gvfs-mtp 7zip

# Multimedia
sudo pacman -S --needed --noconfirm ristretto mpv yt-dlp transmission-gtk newsboat

# Appearance
sudo pacman -S --needed --noconfirm lxappearance nitrogen

# Office
sudo pacman -S --needed --noconfirm libreoffice-still qalculate-gtk

# Fonts
sudo pacman -S --needed --noconfirm ttf-jetbrains-mono ttf-nerd-fonts-symbols

# Extras
sudo pacman -S --needed --noconfirm btop openssh dex fzf rsync

# Printing
sudo pacman -S --needed --noconfirm cups

# Utils
sudo pacman -S --needed --noconfirm bash-completion xdg-user-dirs pacman-contrib numlockx

# Python utils
sudo pacman -S --needed --noconfirm python-dbus-next python-uv python-psutil