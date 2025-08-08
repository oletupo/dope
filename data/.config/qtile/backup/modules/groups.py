from libqtile.config import Group, Key, ScratchPad, DropDown
from libqtile.lazy import lazy

import re
from libqtile.config import Match
from .keys import keys, mod
from .paths import obsidian

# GROUPS
groups = []
group_names = ["1", "2", "3", "4", "5", "6",]
group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ",]
group_layouts = ["ratiotile", "ratiotile", "ratiotile", "ratiotile", "ratiotile", "ratiotile",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))


for i in groups:
    keys.extend([

# CHANGE GROUPS
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        #Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),

# MOVE WINDOW TO SELECTED WORKSPACE AND FOLLOW MOVED WINDOW TO WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])


# SCRATCHPADS

# height width x and y are represented as a fraction of the current screen (0 min, 1 max)
# match is needed because otherwise the window would dissapear instantly

#groups.append(ScratchPad("0",[DropDown("notes", 'alacritty -o "window.opacity=1" -e "btop"', x=0.05, y=0.02, width=0.9, height=0.95, on_focus_lost_hide=True)]))
groups.append(ScratchPad("term",[DropDown("terminal", 'ghostty', opacity=1, x=0, y=0, width=1, height=1)]))

#groups.append(ScratchPad("notes",[DropDown("notes", obsidian, match=Match(wm_class = 'obsidian'), opacity=1, x=0.504, y=0.005, width=0.494, height=0.987, on_focus_lost_hide=False)]))
groups.append(ScratchPad("notes",[DropDown("notes", obsidian, match=Match(wm_class = 'obsidian'), opacity=1, x=0, y=0, width=1, height=1, on_focus_lost_hide=False)]))

keys.append(Key([mod], 'n', lazy.group['notes'].dropdown_toggle('notes')))
keys.append(Key([mod], 't', lazy.group['term'].dropdown_toggle('terminal')))
