import os
import subprocess

from libqtile import qtile
from libqtile import widget, bar
from libqtile.widget import Spacer

from .colors import current_theme
from .paths import myTerm 

# widgets defaults
def init_widgets_defaults():
    return dict(
		font = "Noto Sans Bold", #"JetBrains Mono", Noto Sans Bold
		fontsize = 12,
		padding = 2,
		background = current_theme[0]
		)
widget_defaults = init_widgets_defaults()

# widgets
wdg_wname = widget.WindowName(
	fontsize = 14,
	foreground = current_theme[5],
	background = current_theme[0],
	padding =0,
	scroll=True,
	)
wdg_menu = widget.TextBox(
	fontsize = 20,
	foreground = current_theme[5],
	text = "",
	padding = 0,
	mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('rofi -show drun')}
	)
wdg_updates = widget.GenPollText(
	padding = 0,
	fontsize = 14,
	foreground = current_theme[5],
	background = current_theme[2],
	update_interval= 900,
	func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/scripts/packages.sh")).decode().strip(),
	mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' --hold -e checkupdates')}
	)
wdg_test = widget.GenPollCommand(
	cmd=['echo','hola'], 
	update_interval=1,
	shell=True,
	)
wdg_clock = widget.Clock(
	fontsize = 14,
	foreground = current_theme[5],
	background = current_theme[2],
	padding = 6,
	format = "%d %b, %a [%H:%M:%S]",
	mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' --hold -e cal -3m')}
	)
wdg_miniclock = widget.Clock(
	fontsize = 14,
	foreground = current_theme[5],
	background = current_theme[2],
	padding = 0,
	format = "%Y/%m/%d [%H:%M]",
	mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' --hold -e cal -3m')}
	)
wdg_cpuload = widget.CPU(
	format = '[{load_percent: .0f}%]',
	foreground = current_theme[5],
	background = current_theme[2],
	padding = 3,
	update_interval = 3,
	mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')}
	)
wdg_cputemp = widget.ThermalSensor(
	tag_sensor = 'Tctl', # AMD cpu
	fmt = 'CPU: {}',
	foreground = current_theme[5],
	foreground_alert = current_theme[7],
	background = current_theme[2],
	metric = True,
	padding = 3,
	threshold = 80,
	update_interval = 5
	)
wdg_amd_gputemp = widget.ThermalSensor(
	tag_sensor = 'junction', # AMD
	fmt = 'GPU: {}',
	foreground = current_theme[5],
	foreground_alert = current_theme[7],
	background = current_theme[2],
	metric = True,
	padding = 3,
	threshold = 80,
	update_interval = 5
	)
wdg_ram = widget.Memory(
	format = 'RAM:{MemUsed: .0f}{mm} [{MemPercent: .0f}%]',
	update_interval = 5,
	padding = 3,
	fontsize = 12,
	foreground = current_theme[5],
	background = current_theme[2],
	mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' --hold -e top -o +%MEM')} # top -o +%MEM // free -h
	)		    
wdg_nvidia_gpu = widget.GenPollText( # nvidia
	foreground = current_theme[5],
	background = current_theme[2],
	update_interval= 30, 
	func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/scripts/nvidia-gpu-stats.sh")).decode().strip(),
	mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('nvidia-settings')}
	)		
wdg_net = widget.Net(
	fontsize = 12,
	markup= True,
	interface = "enp0s31f6",
	format = '{down:} ↓↑ {up}',
	prefix= 'M',
	foreground = current_theme[5],
	background = current_theme[2],
	padding = 0,
	update_interval = 3,
	#mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' --hold -e ss -taunp')}
	)
wdg_df = widget.DF(
	fontsize = 12,
	foreground = current_theme[5],
	background = current_theme[2],
	padding = 3,
	visible_on_warn = False,
	partition= '/home',
	format='󰜥 {uf}G [{r: .0f}%]', # 󰜥 󰿠 
	update_interval=300,
	mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' --hold -e df -h')}
	)
wdg_volicon = widget.TextBox(
	foreground = current_theme[5],
	fontsize = 13,
	text = "", #  󰕾
	mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('pavucontrol')}
	)		
wdg_volprct = widget.Volume(
	foreground = current_theme[5],
	background = current_theme[0],
	padding = 0,
	fontsize = 13
	)

# WIDGET DECORATORS
dec_spacer = widget.Spacer(
	background = current_theme[0],
	length = bar.STRETCH,
	)
dec_sep = widget.Sep(
	linewidth = 0,
	padding = 6,
	background = current_theme[0],
	)
dec_fsep = widget.Sep(
	linewidth = 0,
	padding = 120,
	background = current_theme[0],
	)	
dec_angleopen = widget.TextBox(
	fontsize = 32,
	foreground = current_theme[2],
	background = current_theme[0],
	text = "", #  
	padding = 0
	)
dec_angleclose = widget.TextBox(
	fontsize = 32,
	foreground = current_theme[2],
	background = current_theme[0],
	text = "", #  
	padding = 0
	)		
dec_cubeopen = widget.TextBox(
	fontsize = 32,
	foreground = current_theme[2],
	background = current_theme[0],
	text = "",
	padding = 0
	)		
dec_cubeclose = widget.TextBox(
	fontsize = 32,
	foreground = current_theme[2],
	background = current_theme[0],
	text = "",
	padding = 0
	)		
dec_vert = widget.TextBox(
	fontsize = 20,
	foreground = current_theme[9],
	background = current_theme[2],
	text = "", #   󰤃  󰇙 󰿟 󰴼  
	padding = 3,
	)