from libqtile.config import Screen
from libqtile import widget, bar
from libqtile.widget import Spacer

from .colors import current_theme
from .widgets import * # Baby jesus cries (All widgets)

# screen 1 bar composition (long)
def init_widgets_screen1():
    widgets_screen1 = [
		dec_sep,
		#wdg_menu,
		widget.CurrentLayout(
            mode = 'icon',
			foreground = current_theme[5],
			background = current_theme[0],
			scale = 0.6,
			padding = 0
			),
		dec_angleopen,
		wdg_updates,
		dec_angleclose,
		#dec_sep,
		widget.GroupBox(
			font = "Noto Sans Bold",
			fontsize = 12,
			margin_y = 3,
			margin_x = 0,
			padding_y = 6,
			padding_x = 5,
			borderwidth = 5,
			disable_drag = True,
			rounded = False,
			highlight_method = "line",
			active = current_theme[8],
			inactive = current_theme[9],
			highlight_color = current_theme[4],
			this_current_screen_border = current_theme[6],
			other_current_screen_border = current_theme[7],
			this_screen_border = current_theme[6],
			other_screen_border = current_theme[7],
			foreground = current_theme[5],
			background = current_theme[0]
			),
		#dec_sep,
		dec_angleopen,
		wdg_clock,
		dec_angleclose,
		#dec_sep,
		widget.TaskList(
			max_title_width = 0,
			icon_size = None,
			center_aligned = True,
			# max_chars = 1,
			foreground = current_theme[5],
			background = current_theme[0]
			),
		#dec_angleopen,
		#dec_cubeopen,
		#wdg_cpuload,
		#wdg_cputemp,
		#dec_vert,
		#wdg_ram,
		#dec_vert,
		#wdg_gpu,
		#dec_vert,
		#wdg_df,
		#dec_vert,
		#wdg_net,
		#dec_cubeclose,
		#dec_angleclose,
		dec_angleopen,
		#dec_vert,
		wdg_cputemp,
		wdg_cpuload,

		dec_vert,
		wdg_amd_gputemp,
		dec_vert,
		wdg_ram,
		dec_vert,
		wdg_df,
		dec_angleclose,
		widget.Systray(
			background = current_theme[0],
			icon_size = 20,
			padding = 2
			),
		wdg_volicon,
		wdg_volprct,
		dec_sep,
		]
    return widgets_screen1

# screen 2 bar composition (short)
def init_widgets_screen2():
    widgets_screen2 = [	
		dec_sep,
		widget.CurrentLayout(
            mode = 'icon',
			foreground = current_theme[5],
			background = current_theme[0],
			scale = 0.6,
			padding = 0
			),
		dec_sep,
		dec_angleopen,
		wdg_miniclock,
		dec_angleclose,
		dec_sep,
		widget.GroupBox(
			fontsize = 12,
			margin_y = 3,
			margin_x = 0,
			padding_y = 6,
			padding_x = 5,
			borderwidth = 5,
			disable_drag = True,
			rounded = False,
			highlight_method = "line",
			active = current_theme[8],
			inactive = current_theme[9],
			highlight_color = current_theme[4],
			this_current_screen_border = current_theme[6],
			other_current_screen_border = current_theme[7],
			this_screen_border = current_theme[6],
			other_screen_border = current_theme[7],
			foreground = current_theme[5],
			background = current_theme[0]
			),
		#dec_angleopen,
		#wdg_clock,
		#dec_angleclose,
		#dec_sep,

		#dec_cubeopen,
		#dec_vert,
		#dec_vert,
		#wdg_gpu,
		#dec_vert,
		#wdg_net,
		#dec_angleclose,

		#dec_fsep,
		#dec_sep,
		dec_angleopen,
		wdg_cputemp,
		wdg_cpuload,
		dec_vert,
		wdg_ram,
		dec_vert,
		wdg_amd_gputemp,
		
		dec_vert,
		wdg_df,
		dec_angleclose,
		#dec_vert,
		#widget.TaskList(
		#	max_title_width = None,
		#	icon_size = None,
		#	center_aligned = True,
		#	title_width_method
		#	),

		dec_spacer,
		wdg_volicon,
		wdg_volprct,
		dec_sep,
		]
    return widgets_screen2

# screens initialization
def init_screens():
    return [
		Screen(top=bar.Bar(
						widgets=init_widgets_screen1(),
						size=26,
						opacity=1,
						margin=[0,0,0,0],
						x11_drag_polling_rate = 60, # optional default: commented unlimited
				)),
		Screen(top=bar.Bar(
						widgets=init_widgets_screen2(),
						size=26, 
						opacity=1,
						margin=[0,0,0,0],
						x11_drag_polling_rate = 60, # optional default commented unlimited
				)),  # margin [N,E,S,W]
			]
           
screens = init_screens()
