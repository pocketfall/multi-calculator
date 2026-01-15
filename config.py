from utils import normalize_rgba as nrgb

BUTTONS = ["7", "8", "9", "<",
		   "4", "5", "6", "AC",
		   "1", "2", "3", "+",
		   "00", "0", "", "="]

SCREEN_BUTTON_COLORS = {
		"left": nrgb(0, 128, 128, 1),
		"middle": nrgb(255, 127, 80, 1),
		"right": nrgb(255, 223, 0, 1)
		}
SCREENS = ["left", "middle", "right"]
FONT_SIZE = 24
LABEL_TEXT_SIZE = 48
