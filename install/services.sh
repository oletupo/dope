#!/bin/bash

echo "Starting services..."

# NetworkManager
sudo systemctl enable --now NetworkManager.service

# SSD trimming
sudo systemctl enable --now fstrim.timer

# Pacman mirror list updates 
sudo systemctl enable --now reflector.timer

# Printing
sudo systemctl enable --now cups.service

# SSH
sudo systemctl enable --now sshd