#!/bin/bash

Packages=()

# Get CPU vendor ID
vendor=$(lscpu | grep 'Vendor ID' | awk '{print $3}')

# Alternatively (for broader compatibility):
# vendor=$(grep -m 1 'vendor_id' /proc/cpuinfo | awk '{print $3}')

# Act based on CPU vendor
if [[ "$vendor" == "GenuineIntel" ]]; then
    echo "Intel CPU detected."
    Packages+=('intel-ucode')
elif [[ "$vendor" == "AuthenticAMD" ]]; then
    echo "AMD CPU detected."
    Packages+=('amd-ucode')
else
    echo "Unknown CPU vendor: $vendor"
    # Optional fallback action
fi

# Get GPU information using lspci
# This uses lspci, which is typically available by default.
# pkg pciutils
gpu_info=$(lspci | grep -i 'vga\|3d\|display')

# Check for vendor in GPU info
if echo "$gpu_info" | grep -iq 'nvidia'; then
    echo "NVIDIA GPU detected."
    Packages+=('nvidia')
elif echo "$gpu_info" | grep -iq 'amd\|ati'; then
    echo "AMD GPU detected."
    Packages+=('mesa')
    Packages+=('xf86-video-amdgpu')
    Packages+=('vulkan-radeon')
    Packages+=('lib32-vulkan-radeon')
elif echo "$gpu_info" | grep -iq 'intel'; then
    echo "Intel GPU detected."
    Packages+=('mesa')
else
    echo "No known GPU vendor detected (Intel, AMD, NVIDIA)."
fi

sudo pacman -S --needed --noconfirm ${Packages[@]}