#!/bin/bash

echo "Checking prerequisites..."
sudo pacman -Syyu
sudo pacman -S --noconfirm --needed base base-devel linux-firmware linux reflector

# Sort the five most recently synchronized mirrors by download speed and overwrite the local mirrorlist
sudo reflector --latest 5 --sort rate --save /etc/pacman.d/mirrorlist

if [ $? -eq 0 ]
then
  echo "Success!!"
else
  echo "Failure"
fi