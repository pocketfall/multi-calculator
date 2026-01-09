from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from config import BUTTONS, FONT_SIZE

class CalculatorButton(Button):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def my_character(self, button_object):
		print(button_object.text)

class MainLayout(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.orientation = "vertical"

class ButtonGrid(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 4
		self.add_buttons()
	
	def add_buttons(self):
		for button_text in BUTTONS:
			button = self.create_button(button_text)
			self.add_widget(button)

	def create_button(self, button_text, button_func= None):
		button = CalculatorButton(text= button_text, font_size= FONT_SIZE)
		button.bind(on_press= button.my_character)
		return button
