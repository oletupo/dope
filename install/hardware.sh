#!/bin/bash

# Get CPU vendor ID
vendor=$(lscpu | grep 'Vendor ID' | awk '{print $3}')

# Alternatively (for broader compatibility):
# vendor=$(grep -m 1 'vendor_id' /proc/cpuinfo | awk '{print $3}')

# Act based on CPU vendor
if [[ "$vendor" == "GenuineIntel" ]]; then
    echo "Intel CPU detected."
    # Insert Intel-specific actions here
elif [[ "$vendor" == "AuthenticAMD" ]]; then
    echo "AMD CPU detected."
    # Insert AMD-specific actions here
else
    echo "Unknown CPU vendor: $vendor"
    # Optional fallback action
fi

#############################################
# This uses lspci, which is typically available by default.
# pkg pciutils

# Get GPU information using lspci
gpu_info=$(lspci | grep -i 'vga\|3d\|display')

echo "Detected GPU(s):"
echo "$gpu_info"
echo

# Check for vendor in GPU info
if echo "$gpu_info" | grep -iq 'nvidia'; then
    echo "NVIDIA GPU detected."
    # Insert NVIDIA-specific actions here
elif echo "$gpu_info" | grep -iq 'amd\|ati'; then
    echo "AMD GPU detected."
    # Insert AMD-specific actions here
elif echo "$gpu_info" | grep -iq 'intel'; then
    echo "Intel GPU detected."
    # Insert Intel-specific actions here
else
    echo "No known GPU vendor detected (Intel, AMD, NVIDIA)."
fi
