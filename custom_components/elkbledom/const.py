from enum import Enum

DOMAIN = "elkbledom"
CONF_RESET = "reset"
CONF_DELAY = "delay"

class EFFECTS (Enum):
auto_play	=	0x
magic_forward	=	0x
magic_back	=	0x
seven_color_energy	=	0x
seven_color_jump	=	0x
r_g_b_jump	=	0x
y_c_p_jump	=	0x
seven_color_strobe	=	0x
r_g_b_strobe	=	0x
y_c_p_strobe	=	0x
seven_color_gradual	=	0x
r_y_gradual	=	0x
r_p_gradual	=	0x
g_c_gradual	=	0x
g_y_gradual	=	0x
b_p_gradual	=	0x
red_marquee	=	0x
green_marquee	=	0x
blue_marquee	=	0x
yellow_marquee	=	0x
cyan_marquee	=	0x
purple_marquee	=	0x
white_marquee	=	0x
seven_color_race	=	0x
seven_color_race_back	=	0x
r_g_b_race	=	0x
r_g_b_race_back	=	0x
y_c_p_race	=	0x
y_c_p_race_back	=	0x
seven_color_wave	=	0x
seven_color_wave_back	=	0x
r_g_b_wave	=	0x
r_g_b_wave_back	=	0x
y_c_p_wave	=	0x
y_c_p_wave_back	=	0x
seven_color_flush	=	0x
seven_color_flush_back	=	0x
r_g_b_flush	=	0x
r_g_b_flush_back	=	0x
y_c_p_flush	=	0x
y_c_p_flush_back	=	0x
seven_color_flush_close	=	0x
seven_color_flush_open	=	0x
r_g_b_flush_open	=	0x
y_c_p_flush_close	=	0x
y_c_p_flush_open	=	0x

seven_color_close	=	0x
seven_color_open	=	0x
r_g_b_close	=	0x
r_g_b_open	=	0x
y_c_p_close	=	0x
y_c_p_open	=	0x
red_close	=	0x
red_open	=	0x
green_close	=	0x
green_open	=	0x
blue_close	=	0x
blue_close	=	0x
yellow_close	=	0x
yellow_open	=	0x
cyan_close	=	0x
cyan_open	=	0x
purple_close	=	0x
purple_open	=	0x
white_close	=	0x
white_open	=	0x

seven_color_trans	=	0x
seven_color_trans_back	=	0x
r_g_b_trans	=	0x
r_g_b_trans_back	=	0x
y_c_p_trans	=	0x
y_c_p_trans_back	=	0x
six_color_to_red	=	0x
six_color_to_red_back	=	0x
six_color_to_green	=	0x
six_color_to_green_back	=	0x
six_color_to_blue	=	0x
six_color_to_blue_back	=	0x
six_color_to_cyan	=	0x
six_color_to_cyan_back	=	0x
six_color_to_yellow	=	0x
six_color_to_yellow_back	=	0x
six_color_to_purple	=	0x
six_color_to_purple_back	=	0x
six_color_to_white	=	0x
six_color_to_white_back	=	0x
	
seven_color_water	=	0x
seven_color_water_back	=	0x
r_g_b_water	=	0x
r_g_b_water_back	=	0x
y_c_p_water	=	0x
y_c_p_water_back	=	0x
r_g_water	=	0x
r_g_water_back	=	0x
g_b_water	=	0x
g_b_water_back	=	0x
y_b_water	=	0x
y_b_water_back	=	0x
y_c_water	=	0x
y_c_water_back	=	0x
c_p_water	=	0x
c_p_water_back	=	0x
white_water	=	0x
white_water_back	=	0x

w_r_w_flow	=	0x
w_r_w_flow_back	=	0x
w_g_w_flow	=	0x
w_g_w_flow_back	=	0x
w_b_w_flow	=	0x
w_b_w_flow_back	=	0x
w_y_w_flow	=	0x
w_y_w_flow_back	=	0x
w_c_w_flow	=	0x
w_c_w_flow_back	=	0x
w_p_w_flow	=	0x
w_p_w_flow_back	=	0x
r_w_r_flow	=	0x
r_w_r_flow_back	=	0x
g_w_g_flow	=	0x
g_w_g_flow_back	=	0x
b_w_b_flow	=	0x
b_w_b_flow_back	=	0x
y_w_y_flow	=	0x
y_w_y_flow_back	=	0x
c_w_c_flow	=	0x
c_w_c_flow_back	=	0x
p_w_p_flow	=	0x
p_w_p_flow_back	=	0x
	
seven_color_tail	=	0x
seven_color_tail_back	=	0x
red_tail	=	0x
red_tail_back	=	0x
green_tail	=	0x
green_tail_back	=	0x
blue_tail	=	0x
blue_tail_back	=	0x
yellow_tail	=	0x
yellow_tail_back	=	0x
cyan_tail	=	0x
cyan_tail_back	=	0x
purple_tail	=	0x
purple_tail_back	=	0x
white_tail	=	0x
white_tail_back	=	0x

red_running	=	0x
green_running	=	0x
blue_running	=	0x
yellow_running	=	0x
cyan_running	=	0x
purple_running	=	0x
white_running	=	0x
seven_color_running	=	0x
r_g_b_running	=	0x
y_c_p_running	=	0x
b_p_c_y_running	=	0x
b_g_c_y_running	=	0x
red_dot_in_white_running	=	0x
green_dot_in_red_running	=	0x
blue_dot_in_green_running	=	0x
yellow_dot_in_blue_running	=	0x
cyan_dot_in_yellow_running	=	0x
purple_dot_in_cyan_running	=	0x
white_dot_in_purple_running	=	0x
white_dot_in_red_running	=	0x
seven_color_dot_in_red_running	=	0x
seven_color_dot_in_green_running	=	0x
seven_color_dot_in_blue_running	=	0x
seven_color_dot_in_yellow_running	=	0x
seven_color_dot_in_cyan_running	=	0x
seven_color_dot_in_purple_running	=	0x
seven_color_dot_in_white_running	=	0x
green_dot_in_blue_running	=	0x
green_dot_in_red_running	=	0x
red_dot_in_blue_running	=	0x
cyan_dot_in_yellow_running	=	0x
yellow_dot_in_purple_running	=	0x
white_dot_in_yellow_running	=	0x
yellow_dot_in_white_running	=	0x

red_running_back	=	0x
green_running_back	=	0x
blue_running_back	=	0x
yellow_running_back	=	0x
cyan_running_back	=	0x
purple_running_back	=	0x
white_running_back	=	0x
seven_color_running_back	=	0x
r_g_b_running_back	=	0x
y_c_p_running_back	=	0x
b_p_c_y_running_back	=	0x
b_g_c_y_running_back	=	0x
red_dot_in_white_running_back	=	0x
green_dot_in_red_running_back	=	0x
blue_dot_in_green_running_back	=	0x
yellow_dot_in_blue_running_back	=	0x
cyan_dot_in_yellow_running_back	=	0x
purple_dot_in_cyan_running_back	=	0x
white_dot_in_purple_running_back	=	0x
white_dot_in_red_running_back	=	0x
seven_color_dot_in_red_running_back	=	0x
seven_color_dot_in_green_running_back	=	0x
seven_color_dot_in_blue_running_back	=	0x
seven_color_dot_in_yellow_running_back	=	0x
seven_color_dot_in_cyan_running_back	=	0x
seven_color_dot_in_purple_running_back	=	0x
seven_color_dot_in_white_running_back	=	0x
green_dot_in_blue_running_back	=	0x
green_dot_in_red_running_back	=	0x
red_dot_in_blue_running_back	=	0x
cyan_dot_in_yellow_running_back	=	0x
yellow_dot_in_purple_running_back	=	0x
white_dot_in_yellow_running_back	=	0x
yellow_dot_in_white_running_back	=	0x

EFFECTS_list = ['jump_red_green_blue',
    'jump_red_green_blue_yellow_cyan_magenta_white',
    'crossfade_red',
    'crossfade_green',
    'crossfade_blue',
    'crossfade_yellow',
    'crossfade_cyan',
    'crossfade_magenta',
    'crossfade_white',
    'crossfade_red_green',
    'crossfade_red_blue',
    'crossfade_green_blue',
    'crossfade_red_green_blue',
    'crossfade_red_green_blue_yellow_cyan_magenta_white',
    'blink_red',
    'blink_green',
    'blink_blue',
    'blink_yellow',
    'blink_cyan',
    'blink_magenta',
    'blink_white',
    'blink_red_green_blue_yellow_cyan_magenta_white'
    ]

EFFECTS_list_2 = ['----STYLE BASIC----',
    'auto_play',
    'magic_forward',
    'magic_back',
    'seven_color_energy',
	'seven_color_jump',
	'r_g_b_jump',
	'y_c_p_jump',
	'seven_color_strobe',
	'r_g_b_strobe',
	'y_c_p_strobe',
	'seven_color_gradual',
	'r_y_gradual',
	'r_p_gradual',
	'g_c_gradual',
	'g_y_gradual',
	'b_p_gradual',
	'red_marquee',
	'green_marquee',
	'blue_marquee',
	'yellow_marquee',
	'cyan_marquee',
	'purple_marquee',
	'white_marquee',
	'seven_color_race',
	'seven_color_race_back',
	'r_g_b_race',
	'r_g_b_race_back',
	'y_c_p_race',
	'y_c_p_race_back',
	'seven_color_wave',
	'seven_color_wave_back',
	'r_g_b_wave',
	'r_g_b_wave_back',
	'y_c_p_wave',
	'y_c_p_wave_back',
	'seven_color_flush',
	'seven_color_flush_back',
	'r_g_b_flush',
    'r_g_b_flush_back',
	'y_c_p_flush',
 	'y_c_p_flush_back',
	'seven_color_flush_close',
	'seven_color_flush_open',
	'r_g_b_flush_open',
	'y_c_p_flush_close',
 	'y_c_p_flush_open',
	'----STYLE CURTAIN----',
	'seven_color_close',
	'seven_color_open',
	'r_g_b_close',
	'r_g_b_open',
	'y_c_p_close',
	'y_c_p_open',
	'red_close',
	'red_open',
	'green_close',
	'green_open',
	'blue_close',
	'blue_close',
	'yellow_close',
	'yellow_open',
	'cyan_close',
	'cyan_open',
	'purple_close',
	'purple_open',
	'white_close',
	'white_open',
    '----STYLE TRANS----',
	'seven_color_trans',
	'seven_color_trans_back',
	'r_g_b_trans',
	'r_g_b_trans_back',
	'y_c_p_trans',
	'y_c_p_trans_back',
	'six_color_to_red',
	'six_color_to_red_back',
	'six_color_to_green',
	'six_color_to_green_back',
	'six_color_to_blue',
	'six_color_to_blue_back',
	'six_color_to_cyan',
	'six_color_to_cyan_back',
	'six_color_to_yellow',
	'six_color_to_yellow_back',
	'six_color_to_purple',
	'six_color_to_purple_back',
	'six_color_to_white',
	'six_color_to_white_back',
	
    '----STYLE WATER----',
	'seven_color_water',
	'seven_color_water_back',
	'r_g_b_water',
	'r_g_b_water_back',
	'y_c_p_water',
	'y_c_p_water_back',
	'r_g_water',
	'r_g_water_back',
	'g_b_water',
	'g_b_water_back',
	'y_b_water',
	'y_b_water_back',
	'y_c_water',
	'y_c_water_back',
	'c_p_water',
	'c_p_water_back',
	'white_water',
	'white_water_back',
    '----STYLE FLOW----',
	'w_r_w_flow',
	'w_r_w_flow_back',
	'w_g_w_flow',
	'w_g_w_flow_back',
	'w_b_w_flow',
	'w_b_w_flow_back',
	'w_y_w_flow',
	'w_y_w_flow_back',
	'w_c_w_flow',
	'w_c_w_flow_back',
	'w_p_w_flow',
	'w_p_w_flow_back',
	'r_w_r_flow',
	'r_w_r_flow_back',
	'g_w_g_flow',
	'g_w_g_flow_back',
	'b_w_b_flow',
	'b_w_b_flow_back',
	'y_w_y_flow',
	'y_w_y_flow_back',
	'c_w_c_flow',
	'c_w_c_flow_back',
	'p_w_p_flow',
	'p_w_p_flow_back',
	
    '----STYLE TAIL----',
	'seven_color_tail',
	'seven_color_tail_back',
	'red_tail',
	'red_tail_back',
	'green_tail',
	'green_tail_back',
	'blue_tail',
	'blue_tail_back',
	'yellow_tail',
	'yellow_tail_back',
	'cyan_tail',
	'cyan_tail_back',
	'purple_tail',
	'purple_tail_back',
	'white_tail',
	'white_tail_back',
    '----STYLE RUNNING----',
	'red_running',
	'green_running',
	'blue_running',
	'yellow_running',
	'cyan_running',
	'purple_running',
	'white_running',
	'seven_color_running',
	'r_g_b_running',
	'y_c_p_running',
	'b_p_c_y_running',
	'b_g_c_y_running',
	'red_dot_in_white_running',
	'green_dot_in_red_running',
	'blue_dot_in_green_running',
	'yellow_dot_in_blue_running',
	'cyan_dot_in_yellow_running',
	'purple_dot_in_cyan_running',
	'white_dot_in_purple_running',
	'white_dot_in_red_running',
	'seven_color_dot_in_red_running',
	'seven_color_dot_in_green_running',
	'seven_color_dot_in_blue_running',
	'seven_color_dot_in_yellow_running',
	'seven_color_dot_in_cyan_running',
	'seven_color_dot_in_purple_running',
	'seven_color_dot_in_white_running',
	'green_dot_in_blue_running',
	'green_dot_in_red_running',
	'red_dot_in_blue_running',
	'cyan_dot_in_yellow_running',
	'yellow_dot_in_purple_running',
	'white_dot_in_yellow_running',
	'yellow_dot_in_white_running',
    '----STYLE RUNBACK----',
	'red_running_back',
	'green_running_back',
	'blue_running_back',
	'yellow_running_back',
	'cyan_running_back',
	'purple_running_back',
	'white_running_back',
	'seven_color_running_back',
	'r_g_b_running_back',
	'y_c_p_running_back',
	'b_p_c_y_running_back',
	'b_g_c_y_running_back',
	'red_dot_in_white_running_back',
	'green_dot_in_red_running_back',
	'blue_dot_in_green_running_back',
	'yellow_dot_in_blue_running_back',
	'cyan_dot_in_yellow_running_back',
	'purple_dot_in_cyan_running_back',
	'white_dot_in_purple_running_back',
	'white_dot_in_red_running_back',
	'seven_color_dot_in_red_running_back',
	'seven_color_dot_in_green_running_back',
	'seven_color_dot_in_blue_running_back',
	'seven_color_dot_in_yellow_running_back',
	'seven_color_dot_in_cyan_running_back',
	'seven_color_dot_in_purple_running_back',
	'seven_color_dot_in_white_running_back',
	'green_dot_in_blue_running_back',
	'green_dot_in_red_running_back',
	'red_dot_in_blue_running_back',
	'cyan_dot_in_yellow_running_back',
	'yellow_dot_in_purple_running_back',
	'white_dot_in_yellow_running_back',
	'yellow_dot_in_white_running_back'

    ]

class WEEK_DAYS (Enum):
    monday = 0x01
    tuesday = 0x02
    wednesday = 0x04
    thursday = 0x08
    friday = 0x10
    saturday = 0x20
    sunday = 0x40
    all = (0x01 + 0x02 + 0x04 + 0x08 + 0x10 + 0x20 + 0x40)
    week_days = (0x01 + 0x02 + 0x04 + 0x08 + 0x10)
    weekend_days = (0x20 + 0x40)
    none = 0x00

#print(EFFECTS.blink_red.value)
