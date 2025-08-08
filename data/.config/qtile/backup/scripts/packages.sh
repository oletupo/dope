#!/bin/bash

KER="$(uname -r)"
UPDATES="$(checkupdates | wc -l)"
INSTALLED="$(pacman -Q | wc -l)"
PKGSIZE="$(du -sh /var/cache/pacman/pkg | awk '{print $1}')"
echo -e $KER: $INSTALLED[$UPDATES] $PKGSIZE

exit 0
