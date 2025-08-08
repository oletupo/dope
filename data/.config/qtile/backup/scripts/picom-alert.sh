#!/bin/bash

if ! pgrep -x "picom" > /dev/null
then
    notify-send 'Alert: picom off' 
fi

