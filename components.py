from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class CalculatorButton(Button):
	def __init__(self, character, operation):
		super().__init__(text= character)
		self.operation = operation

	def build(self):
		return self

class ButtonGrid(GridLayout):
	def __init__(self):
		super().__init__()
