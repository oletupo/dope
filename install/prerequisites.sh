#!/bin/bash

echo "Installing prerequisites..."
sudo pacman -S --noconfirm --needed base base-devel linux-firmware linux reflector

if [ $? -eq 0 ]
then
  echo "Success!!"
else
  echo "Failure"
fi