import os
import json
from .paths import home

# COLOR PALETTE
def init_theme():
	theme_name = 'theme01' #default
	config_file = home + '/.config/qtile/themes/' + theme_name + '.json'
	if os.path.isfile(config_file):
		with open(config_file) as f:
			dict_theme = json.load(f)
		return [key for key in dict_theme.values()]
	else:
		# fallback to /themes/default.json
		with open(home + '/.config/qtile/themes/default.json') as f:
			dict_theme = json.load(f)
		return [key for key in dict_theme.values()]
	

current_theme = init_theme()
