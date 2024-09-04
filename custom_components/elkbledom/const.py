from enum import Enum

DOMAIN = "elkbledom"
CONF_RESET = "reset"
CONF_DELAY = "delay"

class EFFECTS (Enum):
auto_play	=	0x00
magic_forward	=	0x01
magic_back	=	0x02
seven_color_energy	=	0xd4
seven_color_jump	=	0xc1
r_g_b_jump	=	0xc2
y_c_p_jump	=	0xc3
seven_color_strobe	=	0xc4
r_g_b_strobe	=	0xc5
y_c_p_strobe	=	0xc6
seven_color_gradual	=	0xc7
r_y_gradual	=	0xc8
r_p_gradual	=	0xc9
g_c_gradual	=	0xca
g_y_gradual	=	0xcb
b_p_gradual	=	0xcc
red_marquee	=	0xcd
green_marquee	=	0xce
blue_marquee	=	0xcf
yellow_marquee	=	0xd0
cyan_marquee	=	0xd1
purple_marquee	=	0xd2
white_marquee	=	0xd3
seven_color_race	=	0x4d
seven_color_race_back	=	0x4e
r_g_b_race	=	0x4f
r_g_b_race_back	=	0x50
y_c_p_race	=	0x51
y_c_p_race_back	=	0x52
seven_color_wave	=	0x53
seven_color_wave_back	=	0x54
r_g_b_wave	=	0x55
r_g_b_wave_back	=	0x56
y_c_p_wave	=	0x57
y_c_p_wave_back	=	0x58
seven_color_flush	=	0xb5
seven_color_flush_back	=	0xb6
r_g_b_flush	=	0xb7
r_g_b_flush_back	=	0xb8
y_c_p_flush	=	0xb9
y_c_p_flush_back	=	0xba
seven_color_flush_close	=	0xbb
seven_color_flush_open	=	0xbc
r_g_b_flush_close	=	0xbd
r_g_b_flush_open	=	0xbe
y_c_p_flush_close	=	0xbf
y_c_p_flush_open	=	0xc0
seven_color_close	=	0x39
seven_color_open	=	0x3a
r_g_b_close	=	0x3b
r_g_b_open	=	0x3c
y_c_p_close	=	0x3d
y_c_p_open	=	0x3e
red_close	=	0x3f
red_open	=	0x40
green_close	=	0x41
green_open	=	0x42
blue_close	=	0x43
blue_close	=	0x44
yellow_close	=	0x45
yellow_open	=	0x46
cyan_close	=	0x47
cyan_open	=	0x48
purple_close	=	0x49
purple_open	=	0x4a
white_close	=	0x4b
white_open	=	0x4c
seven_color_trans	=	0x03
seven_color_trans_back	=	0x04
r_g_b_trans	=	0x05
r_g_b_trans_back	=	0x06
y_c_p_trans	=	0x07
y_c_p_trans_back	=	0x08
six_color_to_red	=	0x09
six_color_to_red_back	=	0x0a
six_color_to_green	=	0x0b
six_color_to_green_back	=	0x0c
six_color_to_blue	=	0x0d
six_color_to_blue_back	=	0x0e
six_color_to_cyan	=	0x0f
six_color_to_cyan_back	=	0x10
six_color_to_yellow	=	0x11
six_color_to_yellow_back	=	0x12
six_color_to_purple	=	0x13
six_color_to_purple_back	=	0x14
six_color_to_white	=	0x15
six_color_to_white_back	=	0x16
seven_color_water	=	0x27
seven_color_water_back	=	0x28
r_g_b_water	=	0x29
r_g_b_water_back	=	0x2a
y_c_p_water	=	0x2b
y_c_p_water_back	=	0x2c
r_g_water	=	0x2d
r_g_water_back	=	0x2e
g_b_water	=	0x2f
g_b_water_back	=	0x30
y_b_water	=	0x31
y_b_water_back	=	0x32
y_c_water	=	0x33
y_c_water_back	=	0x34
c_p_water	=	0x35
c_p_water_back	=	0x36
white_water	=	0x37
white_water_back	=	0x38
w_r_w_flow	=	0x8f
w_r_w_flow_back	=	0x90
w_g_w_flow	=	0x91
w_g_w_flow_back	=	0x92
w_b_w_flow	=	0x93
w_b_w_flow_back	=	0x94
w_y_w_flow	=	0x95
w_y_w_flow_back	=	0x96
w_c_w_flow	=	0x97
w_c_w_flow_back	=	0x98
w_p_w_flow	=	0x99
w_p_w_flow_back	=	0x9a
r_w_r_flow	=	0x9b
r_w_r_flow_back	=	0x9c
g_w_g_flow	=	0x9d
g_w_g_flow_back	=	0x9e
b_w_b_flow	=	0x9f
b_w_b_flow_back	=	0xa0
y_w_y_flow	=	0xa1
y_w_y_flow_back	=	0xa2
c_w_c_flow	=	0xa3
c_w_c_flow_back	=	0xa4
p_w_p_flow	=	0xa5
p_w_p_flow_back	=	0xa6
seven_color_tail	=	0x17
seven_color_tail_back	=	0x18
red_tail	=	0x19
red_tail_back	=	0x1a
green_tail	=	0x1b
green_tail_back	=	0x1c
blue_tail	=	0x1d
blue_tail_back	=	0x1e
yellow_tail	=	0x1f
yellow_tail_back	=	0x20
cyan_tail	=	0x21
cyan_tail_back	=	0x22
purple_tail	=	0x23
purple_tail_back	=	0x24
white_tail	=	0x25
white_tail_back	=	0x26
red_running	=	0x59
green_running	=	0x5b
blue_running	=	0x5d
yellow_running	=	0x5f
cyan_running	=	0x61
purple_running	=	0x63
white_running	=	0x65
seven_color_running	=	0x67
r_g_b_running	=	0x69
y_c_p_running	=	0x6b
b_p_c_y_running	=	0x6d
b_g_c_y_running	=	0x6f
red_dot_in_white_running	=	0x71
green_dot_in_red_running	=	0x73
blue_dot_in_green_running	=	0x75
yellow_dot_in_blue_running	=	0x77
cyan_dot_in_yellow_running	=	0x79
purple_dot_in_cyan_running	=	0x7b
white_dot_in_purple_running	=	0x7d
white_dot_in_red_running	=	0x7f
seven_color_dot_in_red_running	=	0x81
seven_color_dot_in_green_running	=	0x83
seven_color_dot_in_blue_running	=	0x85
seven_color_dot_in_yellow_running	=	0x87
seven_color_dot_in_cyan_running	=	0x89
seven_color_dot_in_purple_running	=	0x8b
seven_color_dot_in_white_running	=	0x8d
green_dot_in_blue_running	=	0xa7
green_dot_in_red_running	=	0xa9
red_dot_in_blue_running	=	0xab
cyan_dot_in_yellow_running	=	0xad
yellow_dot_in_purple_running	=	0xaf
white_dot_in_yellow_running	=	0xb1
yellow_dot_in_white_running	=	0xb3
red_running_back	=	0x5a
green_running_back	=	0x5c
blue_running_back	=	0x5e
yellow_running_back	=	0x60
cyan_running_back	=	0x62
purple_running_back	=	0x64
white_running_back	=	0x66
seven_color_running_back	=	0x68
r_g_b_running_back	=	0x6a
y_c_p_running_back	=	0x6c
b_p_c_y_running_back	=	0x6e
b_g_c_y_running_back	=	0x70
red_dot_in_white_running_back	=	0x72
green_dot_in_red_running_back	=	0x74
blue_dot_in_green_running_back	=	0x76
yellow_dot_in_blue_running_back	=	0x78
cyan_dot_in_yellow_running_back	=	0x7a
purple_dot_in_cyan_running_back	=	0x7c
white_dot_in_purple_running_back	=	0x7e
white_dot_in_red_running_back	=	0x80
seven_color_dot_in_red_running_back	=	0x82
seven_color_dot_in_green_running_back	=	0x84
seven_color_dot_in_blue_running_back	=	0x86
seven_color_dot_in_yellow_running_back	=	0x88
seven_color_dot_in_cyan_running_back	=	0x8a
seven_color_dot_in_purple_running_back	=	0x8c
seven_color_dot_in_white_running_back	=	0x8e
green_dot_in_blue_running_back	=	0xa8
green_dot_in_red_running_back	=	0xaa
red_dot_in_blue_running_back	=	0xac
cyan_dot_in_yellow_running_back	=	0xae
yellow_dot_in_purple_running_back	=	0xb0
white_dot_in_yellow_running_back	=	0xb2
yellow_dot_in_white_running_back	=	0xb4

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
    'Autoplay',
    'Magic Forward',
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
