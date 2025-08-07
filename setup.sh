#!/bin/bash

# Store the current working directory in a variable
BASE_DIR=$(pwd)

# Print the stored directory
echo "Current directory is: $BASE_DIR"

# Install prerequisites
source $BASE_DIR/install/prerequisites.sh

# Install hardware dependant drivers (Intel/Nvidia/AMD)
source $BASE_DIR/install/hardware.sh

# Install AUR helper
source $BASE_DIR/install/aur.sh

# Install and configure display manager
source $BASE_DIR/install/displaymanager.sh $BASE_DIR

# Install base applications
source $BASE_DIR/install/applications.sh

# Starting services
#source $BASE_DIR/install/services.sh

# Copying dotfiles
#source $BASE_DIR/install/dotfiles.sh

# Setting themes and fonts
#source $BASE_DIR/install/themes.sh

# Setting credentials
#source $BASE_DIR/install/credentials.sh

# Setting folders and file asociations
#source $BASE_DIR/install/mimetypes.sh

# Reboot
echo "Setup completed!! rebooting now"