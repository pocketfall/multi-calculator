from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
from config import BUTTONS, FONT_SIZE

class Interface(PageLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

class MainLayout(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.orientation = "vertical"

class ButtonGrid(GridLayout):
	def __init__(self, button_func, **kwargs):
		super().__init__(**kwargs)
		self.cols = 4

		self.add_buttons(button_func)
	
	def add_buttons(self, button_func) -> None:
		for button_text in BUTTONS:
			button = Button(text= button_text,
				   font_size= FONT_SIZE,
				   on_press= button_func)
			self.add_widget(button)
