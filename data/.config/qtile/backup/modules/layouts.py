import re

from libqtile.config import Match, MatchAll
from libqtile import layout
from .colors import current_theme

def init_layout_theme():
    return {
		"margin":1,
		"border_width":4,
		"border_focus": current_theme[3], # Unico uso
		"border_normal": current_theme[9]
		}

layout_theme = init_layout_theme()

# LAYOUTS
layouts = [
    layout.RatioTile(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Bsp(**layout_theme),   
    #layout.Max(**layout_theme),
    #layout.Stack(num_stacks=2),
    #layout.Zoomy(),
    #layout.TreeTab(sections=['Tabs:'], panel_width=85, bg_color="#2F343F", fontsize=10, place_right=True),
    layout.Floating(margin=3, border_width=1, border_focus="#fba922", border_normal="#fba922"),
]

# Floating windows rules
floating_types = ["notification", "toolbar", "splash", "dialog"] # "rename"
# Run the utility of `xprop` to see the wm class and name of an X client.
# It can match by title, wm_class, role, wm_type, wm_instance_class, net_wm_pid, or wid.
thunar_floating_rules = ['Error', 'Confirm to replace files', 'New Empty File...','Create New Folder']
steam_floating_rules = ['Special Offers','Launching...']
floating_layout = layout.Floating(float_rules=[
	Match(wm_class = 'qalculate-gtk'),
    Match(wm_class = 'xfce4-terminal'),
    Match(wm_class = 'pavucontrol'),
    Match(wm_class = 'nitrogen'),
    Match(title = 'P-Dal Capture'),
    Match(title = 'Torrent Options'), # Transmission 
    Match(role = 'GtkFileChooserDialog'), # GTK Save Dialog 
    Match(role = 'PictureInPicture'), # Firefox detached video window 
    Match(title = 'Picture in picture'), # Chrome detached video window

    # Thunar floating rules (TODO: combine into one rule)
    MatchAll(Match(wm_class = 'Thunar'), Match(title = re.compile(r'\bRename.'))), # Thunar rename
    MatchAll(Match(wm_class = 'Thunar'), Match(title = 'Error')), # Thunar error
    MatchAll(Match(wm_class = 'Thunar'), Match(title = 'Confirm to replace files')), # Thunar replace
    MatchAll(Match(wm_class = 'Thunar'), Match(title = 'New Empty File...')), # Thunar new file
    MatchAll(Match(wm_class = 'Thunar'), Match(title = 'Create New Folder')), # Thunar new folder
    # Steam
    MatchAll(Match(wm_class = 'steamwebhelper'), Match(title = 'Special Offers')), # Steam adds
    MatchAll(Match(wm_class = 'steamwebhelper'), Match(title = 'Launching...')), # Steam launch
    
    MatchAll(Match(wm_class = 'geany'), Match(title = 'Question')), # Geany
    MatchAll(Match(wm_class = 'soffice'), Match(title = 'Save Document?')), # Libreoffice save
    MatchAll(Match(wm_class = 'qBittorrent'), Match(title = 'Remove torrent(s)')), # qBittorrent remove
    ], border_focus = current_theme[3])

