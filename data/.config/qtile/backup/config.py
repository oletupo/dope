import os
import subprocess

# qtile imports
from libqtile import qtile
from libqtile.lazy import lazy
from libqtile import hook
#from libqtile.config import Key, Screen, Group, Click, Rule, KeyChord, Match

# qtile/modules imports
from modules.paths import home
from modules.keys import mod, mod1, mod2, keys
from modules.mouse import mouse
from modules.groups import groups
from modules.colors import current_theme
from modules.layouts import layouts, floating_layout, floating_types
from modules.screens import screens
from modules.widgets import widget_defaults
from modules.hooks import start_once, start_always, set_floating, configuration_backup, current_screen_change, change_layout_on_group_change


# default config: https://docs.qtile.org/en/latest/manual/config/default.html
# logfile: ~/.local/share/qtile

main = None
dgroups_key_binder = None
dgroups_app_rules = []
#floating_types = ["notification", "toolbar", "splash", "dialog"] # "rename"
floats_keep_above = True
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False

focus_on_window_activation = "smart" # focus or smart
wmname = "LG3D"
