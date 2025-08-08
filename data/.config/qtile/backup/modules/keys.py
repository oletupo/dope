from libqtile.config import Key
from libqtile.lazy import lazy

from .paths import home, myTerm, rofi_list_windows, rofi_drun, rofi_file_find, rofi_power_menu, obsidian, rofi_pkg_search
from .lazyutils import go_to_empty_group, tidygroups, window_to_prev_group, send_window_to_empty_group, active_window_info, swap_groups_between_screens

mod = "mod4" #  mod4 or mod = super key
mod1 = "alt"
mod2 = "control"

# KEYBINDINGS
''' Special Keys https://github.com/qtile/qtile/blob/master/libqtile/backend/x11/xkeysyms.py 
    BackSpace, Home, End, comma, colon, semicolon, underscore,'''
keys = [
    Key([], "Print", lazy.spawn('xfce4-screenshooter')),

	# SUPER + KEYS
    Key([mod], "w", lazy.window.kill()),
    Key([mod], "q", lazy.window.toggle_floating()),
    Key([mod], "e", lazy.spawn('Thunar')), 
    Key([mod], "r", lazy.layout.flip()), # flip layout for monadtall/monadwide
    #Key([mod], "t", lazy.spawn('ghostty')), # used with that key but added as a scrathcpad
     
    Key([mod], "a", lazy.spawn(myTerm + ' -e ranger')), 
    Key([mod], "s", lazy.spawn(rofi_pkg_search)),
    Key([mod], "d", lazy.spawn(rofi_drun)),
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    # my lazy functions
    Key([mod], "z", go_to_empty_group()()),
    Key([mod], "x", send_window_to_empty_group()),
    Key([mod], "c", swap_groups_between_screens()),
    Key([mod], "v", lazy.function(tidygroups)),

    Key([mod], "i", active_window_info()),
    #Key([mod], "o", active_window_info()),     
    #Key([mod], "p", window_to_prev_group()),  

    Key([mod], "period", lazy.screen.next_group(skip_empty=True)),
    Key([mod], "comma", lazy.screen.prev_group(skip_empty=True)), 
    Key([mod], "space", lazy.next_screen()), # picom crashes when focusing an empty workspace

    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "Return", lazy.spawn(myTerm)),
	Key([mod], "Tab", lazy.next_layout()),

    # SUPER + KEYPAD
    Key([mod], "KP_Insert", lazy.restart()), # KeyPad 0
    Key([mod], "KP_Subtract", lazy.spawn(rofi_power_menu)), # KeyPad -
    Key([mod], "KP_Add", lazy.spawn('pavucontrol')), # KeyPad +

	# SUPER + SHIFT + KEYS
    Key([mod, "shift"], "q", lazy.spawn('qalculate-gtk')),
    Key([mod, "shift"], "w", lazy.spawn('geany')),
    Key([mod, "shift"], "e", lazy.spawn('code')),

    Key([mod, "shift"], "a", lazy.spawn('firefox')),
    Key([mod, "shift"], "s", lazy.spawn(obsidian)),
    Key([mod, "shift"], "d", lazy.spawn('chromium -no-default-browser-check')),

    Key([mod, "shift"], "Return", lazy.spawn('Thunar')),
	
    # SUPER + CTRL KEYS
    #Key([mod, "control"], "s", lazy.spawn('libreoffice')),
   	
    # CONTROL KEYS
	#Key([mod1], "z", lazy.next_screen()),
	
    # ALT KEYS
	Key(["mod1"], "Tab", lazy.spawn(rofi_list_windows)),

    # CONTROL-ALT KEYS
    Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
    Key(["mod1", "control"], "p", lazy.spawn(rofi_power_menu)),
    Key(["mod1", "control"], "q", lazy.shutdown()),

	# ALT + Fx KEYS
    #Key(["mod1"], "F2", lazy.spawn('gmrun')),

	# CONTROL + SHIFT KEYS
    #Key([mod2, "shift"], "Escape", lazy.spawn('xfce4-taskmanager')),
	
    # MULTIMEDIA KEYS
    # INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),
    
    # INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
	#Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
	#Key([], "XF86AudioNext", lazy.spawn("mpc next")),
	#Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
	#Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

	# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

	# RESIZE UP, DOWN, LEFT, RIGHT
	# Commented lazy.layouts generate errors on qtiles logfile
    Key([mod, "control"], "l",
        #lazy.layout.grow_right(),
        lazy.layout.grow(),
        #lazy.layout.increase_ratio(),
        #lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        #lazy.layout.grow_right(),
        lazy.layout.grow(),
        #lazy.layout.increase_ratio(),
        #lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        #lazy.layout.grow_left(),
        lazy.layout.shrink(),
        #lazy.layout.decrease_ratio(),
        #lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        #lazy.layout.grow_left(),
        lazy.layout.shrink(),
        #lazy.layout.decrease_ratio(),
        #lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        #lazy.layout.grow_up(),
        lazy.layout.grow(),
        #lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        #lazy.layout.grow_up(),
        lazy.layout.grow(),
        #lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        #lazy.layout.grow_down(),
        lazy.layout.shrink(),
        #lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        #lazy.layout.grow_down(),
        lazy.layout.shrink(),
        #lazy.layout.increase_nmaster(),
        ),

	# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),
	# FUNCTION KEYS
    Key([], "F12", lazy.spawn('xfce4-terminal --drop-down')),
    
    # BSP
	# FLIP LAYOUT FOR BSP
	#Key([mod, "mod1"], "k", lazy.layout.flip_up()),
	#Key([mod, "mod1"], "j", lazy.layout.flip_down()),
	#Key([mod, "mod1"], "l", lazy.layout.flip_right()),
	#Key([mod, "mod1"], "h", lazy.layout.flip_left()),
	# MOVE WINDOWS UP OR DOWN BSP LAYOUT
	#Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
	#Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
	#Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
	#Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ]
