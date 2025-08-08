import os

# PATHS
home = os.path.expanduser('~')
myTerm = "alacritty"

# Rofi commands
rofi_list_windows = 'rofi -show window \
    -font "JetBrains NF 18" \
    -i \
    -l 3\
    -theme-str "window {width: 33em;} listview {lines: 10;}"'

rofi_drun = 'rofi -show drun \
    -font "JetBrains NF 18" \
    -theme-str "window {width: 21em;}"'

rofi_file_find = 'rofi  -show find \
    -modi find:~/.config/rofi/scripts/file-finder \
    -width 1600'

# fstring can mess things up
# -modi "menu:~/.config/rofi/scripts/power-menu --choices=reboot/shutdown/logout/suspend --no-symbols" (without icons)
rofi_power_menu = 'rofi  -show menu \
-modi "menu:~/.config/rofi/scripts/power-menu --choices=reboot/shutdown/logout/suspend " \
-config "~/.config/rofi/themes/Pmenu.rasi" \
-font "JetBrains NF 20" \
-theme-str "window {width: 12em;}"'

# Appimages
# problemas con cambio de version appimg
#notes_app = '~/Applications/Obsidian-1.5.8.AppImage' 

# Scripts called from .desktop files
obsidian = f'dex {home}/.local/share/applications/appimage-obsidian.desktop'
rofi_pkg_search = f'dex {home}/.local/share/applications/rofi-archweb.desktop'
#kill_pid = f'dex {home}/.local/share/applications/ropy-kill.desktop'

