from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from config import BUTTONS, FONT_SIZE


class MainLayout(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.orientation = "vertical"

class ButtonGrid(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 4
	
