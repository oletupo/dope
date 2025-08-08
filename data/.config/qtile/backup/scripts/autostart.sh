#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

# xrandr 
xrandr --output HDMI-A-0 --mode 2560x1440 --rate 60.0
# vertical monitor setup
xrandr --output HDMI-A-1 --rotate right

# keyboard 
setxkbmap -layout es
numlockx on &

# starting utility applications at boot time
run nm-applet &
udiskie -t &
picom -b --config $HOME/.config/picom/picom.conf 

# polkit and notifications
dunst &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# starting user applications at boot time
nitrogen --restore &
