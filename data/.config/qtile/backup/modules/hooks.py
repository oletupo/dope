import os
import subprocess

from libqtile import hook, layout, qtile

# requires python-dbus-next
from libqtile.utils import send_notification
from .layouts import floating_types, layout_theme


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for() or window.window.get_wm_type() in floating_types):
        window.floating = True
'''
Once startup is completed lauches backup script saving working config to qtile/backup folder
'''
@hook.subscribe.startup_complete
def configuration_backup():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/qbackup.sh'])
    # python3 ~/.config/qtile/config.py && qtile cmd-obj -o cmd -f validate_config

'''
Checks for picom process state and sends notification if down
'''
@hook.subscribe.current_screen_change
def current_screen_change():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/picom-alert.sh'])

'''
Gives basic window info notifications (screen, group and layout) of the focused window
window_info_toggle must be true to display info
Uses exceptions to avoid on first load (works anyway):
screen_index = qtile.screens.index(qtile.current_screen)
ValueError: <libqtile.config.Screen object at 0x7f946c7dbec0> is not in list
'''
@hook.subscribe.setgroup
def window_info_notify():
    window_info_toggle = False
    group = qtile.current_group
    try:
        group_index = qtile.groups.index(qtile.current_group)
        screen_index = qtile.screens.index(qtile.current_screen)
        layout_name = group.layout.name
        if window_info_toggle:
            send_notification("qtile", f" Screen: {screen_index} Group: {group_index+1} Layout: {layout_name}")
    except ValueError:
        pass

'''
Changes layout depending on the screen,
on screen 0 (horizontal) set monadtall, on screen 1 (vertical) set monadwide 
Uses exceptions to avoid on first load (works anyway):
screen_index = qtile.screens.index(qtile.current_screen)
ValueError: <libqtile.config.Screen object at 0x7f946c7dbec0> is not in list
'''
@hook.subscribe.setgroup
def change_layout_on_group_change():
    group = qtile.current_group
    try:
        screen_index = qtile.screens.index(qtile.current_screen)
        if screen_index == 1:
            group.setlayout('monadwide')
        else:
            group.setlayout('monadtall')
    except ValueError:
        pass