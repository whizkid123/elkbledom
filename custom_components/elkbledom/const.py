from enum import Enum

DOMAIN = "elkbledom"
CONF_RESET = "reset"
CONF_DELAY = "delay"

class EFFECTS (Enum):
    jump_red_green_blue = 0x87
    jump_red_green_blue_yellow_cyan_magenta_white = 0x88
    crossfade_red = 0x8b
    crossfade_green = 0x8c
    crossfade_blue = 0x8d
    crossfade_yellow = 0x8e
    crossfade_cyan = 0x8f
    crossfade_magenta = 0x90
    crossfade_white = 0x91
    crossfade_red_green = 0x92
    crossfade_red_blue = 0x93
    crossfade_green_blue = 0x94
    crossfade_red_green_blue = 0x89
    crossfade_red_green_blue_yellow_cyan_magenta_white = 0x8a
    blink_red = 0x96
    blink_green = 0x97
    blink_blue = 0x98
    blink_yellow = 0x99
    blink_cyan = 0x9a
    blink_magenta = 0x9b
    blink_white = 0x9c
    blink_red_green_blue_yellow_cyan_magenta_white = 0x95

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
    'power off', 'y-c-p flush open',
    'y-c-p flush close',
    'r-g-b flush close',
	'7-color open',
	'7-color close',
	'y-c-p flush back',
	'y-c-p flush',
	'r-g-b flush back',
	'r-g-b flush',
	'7-color flush back',
	'7-color flush',
	'y-c-p wave back',
	'y-c-p wave',
	'r-g-b wave back',
	'r-g-b wave',
	'7-color wave back',
	'7-color wave',
	'y-c-p race back',
	'y-c-p race',
	'r-g-b race back',
	'r-g-b race',
	'7-color race back',
	'7-color race',
	'white marquee',
	'purple marquee',
	'cyan marquee',
	'yellow marquee',
	'blue marquee',
	'green marquee',
	'red marquee',
	'b-p gradual',
	'g-y gradual',
	'g-c gradual',
	'r-p gradual',
	'r-y gradual',
	'7-color gradual',
	'y-c-p strobe',
    'r-g-b strobe',
	'7-color strobe',
 	'y-c-p jump',
	'r-g-b jump',
	'7-color jump',
	'7-color energy',
	'magic back',
 	'magic forward',
	'autoplay',
	'----STYLE CURTAIN----',
    '----STYLE TRANS----',
    '----STYLE WATER----',
    '----STYLE FLOW----',
    '----STYLE TAIL----',
    '----STYLE RUN----',
    '----STYLE RUNBACK----'

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
