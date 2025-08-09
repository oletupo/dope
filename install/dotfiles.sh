#!/bin/bash

# Getting path from arguments
BASE_DIR="$1"

echo "Setting bashrc..."
cp -f $BASE_DIR/data/.bashrc ~/.bashrc

echo "Copying dotfiles..."
cp -rf $BASE_DIR/data/.config ~/"