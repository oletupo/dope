#!/bin/bash

# Ruta del directorio a verificar
BACKUPFOLDER="$HOME/.config/qtile/backup"

# Comprobar si el directorio existe
if [ ! -d "$BACKUPFOLDER" ]; then
    mkdir -p "$BACKUPFOLDER"
fi

# Copia de archivos de configuracion
cp -f $HOME/.config/qtile/config.py $HOME/.config/qtile/backup/config.py
cp -Rf $HOME/.config/qtile/modules $HOME/.config/qtile/backup/
cp -Rf $HOME/.config/qtile/scripts $HOME/.config/qtile/backup/

notify-send 'qtile configuration saved on .config/qtile/backup'
