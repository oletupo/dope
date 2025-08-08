#!/bin/bash

cp -f $HOME/.config/qtile/backup/config.py $HOME/.config/qtile/config.py
cp -Rf $HOME/.config/qtile/backup/modules $HOME/.config/qtile/
cp -Rf $HOME/.config/qtile/backup/scripts $HOME/.config/qtile/

notify-send 'qtile configuration restored from .config/qtile/backup'
