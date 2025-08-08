from libqtile.lazy import lazy
from libqtile.scratchpad import ScratchPad
from libqtile.utils import send_notification

import os
import subprocess
# https://docs.qtile.org/en/latest/manual/config/lazy.html#examples
'''
Active window info
'''
@lazy.function
def active_window_info(qtile):
    # Obtener la ventana activa
    current_window = qtile.current_window
    subprocess.Popen(['notify-send', str(current_window)])
    return

'''
Swap active groups between screens 
'''
@lazy.function
def swap_groups_between_screens(qtile):
    # Obtener las dos pantallas
    screen0 = qtile.screens[0]
    screen1 = qtile.screens[1]
    
    # Obtener el grupo activo en cada pantalla
    group0 = screen0.group
    group1 = screen1.group
    
    # Intercambiar los grupos entre las pantallas
    screen0.set_group(group1)
    screen1.set_group(group0)

'''
Send current window to empty group
La función obtiene la ventana activa (current_window) y verifica si hay ventanas activas para continuar.
Luego, recorre todos los grupos (escritorios) buscando el primero que esté vacío (if not group.windows).
Si encuentra un grupo vacío, mueve la ventana al grupo con current_window.togroup(group.name)
y cambia el foco al grupo con qtile.groups_map[group.name].toscreen().
'''
@lazy.function
def send_window_to_empty_group(qtile):
    # Obtener la ventana activa
    current_window = qtile.current_window
    # Si no hay ventana activa, salir
    if not current_window:
        return

    # Recorrer los grupos (escritorios)
    for group in qtile.groups:
        # Comprobar si el grupo está vacío
        if not group.windows:
            # Mover la ventana activa al grupo vacío
            current_window.togroup(group.name)
            # Cambiar al grupo vacío
            qtile.groups_map[group.name].toscreen()
            break

'''
Go to the first empty group
https://github.com/qtile/qtile/discussions/3667

Usage:
    from utils import go_to_empty_group
    Key([mod], "space", go_to_empty_group()),
'''
@lazy.function
def go_to_empty_group(qtile):
    for group in qtile.groups:
        if not group.windows:
            qtile.current_screen.set_group(group)
            break

'''
Send focused window to previous or next group
todo:  loop on overflow
https://github.com/SpyrosRoum/qtile-config/blob/568b2169b8b6e1615bd8bd17d2c3db1350c7d64f/modules/lazy_functions.py
'''
@lazy.window.function
def window_to_prev_group(window):
    index = window.qtile.groups.index(window.group)
    index = (index - 1) % len(window.qtile.groups)
    window.cmd_togroup(window.qtile.groups[index].name)

@lazy.window.function
def window_to_next_group(window):
    index = window.qtile.groups.index(window.group)
    index = (index + 1) % len(window.qtile.groups)
    window.cmd_togroup(window.qtile.groups[index].name)

"""
Move windows to the leftmost empty groups.
For example, if you have windows on groups 2, 4 and 6,
running this command will move windows to groups 1, 2 and 3.
If follow_focus is True (default) the current window will remain focused
and the the group containing that window will be focused.
If match_layout is True (default) the layout in the destination will be changed
to match the layout of the group being moved but only if that layout is available
in the group. NB this only matches layouts by name so different configurations of
the same layout may not be matched.
Scratchpad windows are not moved.
Usage:
    from utils import tidygroups
    keys.extend([
        Key([mod, "shift"], 't', lazy.function(tidygroups)),
        Key([mod, "control"], 't', lazy.function(tidygroups, follow_focus=False))
    ])    
"""

def tidygroups(qtile, follow_focus: bool = True, match_layout: bool = True) -> None:
    def match_layout_name(current, destination) -> str | None:
        layouts = (
            layout.name
            for layout in destination.layouts
            if layout.name == current.layout.name
        )
        return next(layouts, None)

    win = qtile.current_window
    empty = []

    for group in qtile.groups:

        # We need to skip scratchpads
        if isinstance(group, ScratchPad):
            continue

        # If the group is empty, add it to the list of empty groups
        # and then move on to the next group
        if not group.windows:
            empty.append(group)
            continue

        # If we have an empty group available and the current group has
        # windows then we can start moving windows.
        if empty and group.windows:

            # Get the first available empty group
            destination = empty.pop(0)

            if match_layout:
                # Let's see if we can match the current layout in the destination
                layout = match_layout_name(group, destination)

                if layout is not None and layout != destination.layout.name:
                    destination.cmd_setlayout(layout)

            # We iterate over a copy of the windows list as we're modifying the original
            for window in group.windows.copy():
                if group is qtile.current_group:
                    window.hide()
                group.remove(window)
                destination.add(window)

            # This group is now empty so we can add it to the list of empty groups
            empty.append(group)

    # Set focus to group containing the previously focused window
    if follow_focus and win is not None:
        win.group.cmd_toscreen()
        win.focus(False)

@lazy.window.function
def manual_save_configuration():
    try:
        home = os.path.expanduser('~')
        # python3 ~/.config/qtile/config.py && qtile cmd-obj -o cmd -f validate_config
        subprocess.Popen(['python3', '~/.config/qtile/config.py', '&&', 'qtile', 'cmd-obj', '-o', 'cmd', '-f', 'validate_config'])
        subprocess.call([home + '/.config/qtile/scripts/qbackup.sh'])
        send_notification("qtile", f"qtile configuration saved")
    except:
        pass
