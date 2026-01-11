from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from components import ButtonGrid, MainLayout
from config import BUTTONS, FONT_SIZE

class TheApp(App):
	def build(self):
		self.title = "Calculator Maximum"
		self.label_text = "0"
		self.numbers = []
		layout = self.create_layout()
		return layout

	def create_layout(self) -> MainLayout:
		layout = MainLayout()
		self.label = self.create_label()
		layout.add_widget(self.label)
		calculator_grid = self.create_calculator()
		layout.add_widget(calculator_grid)
		return layout
	
	def create_calculator(self) -> ButtonGrid:
		buttons = ButtonGrid(size_hint= [1, .8])
		for button_text in BUTTONS:
			button = Button(text= button_text, 
				   on_press= self.add_to_display, 
				   font_size= FONT_SIZE) 
			buttons.add_widget(button)
		return buttons

	def add_to_display(self, button_object):
		button_text = button_object.text
		print(button_text)
		if button_text != "=":
			match button_text:
				case "BORRAR":
					self.delete_character()
				case _:
					self.label.text = button_text if self.label.text == "0" else self.label.text + button_text
		else:
			self.do_math()
	
	def do_math(self):
		print("doing math here")
		# TODO:
		# clear label text on screen

		# TODO
		# turn string into list and get numbers from it

		# TODO
		# do the actual math

	
	def delete_character(self):
		self.label_text = self.label.text[:-1]
		self.label.text = self.label_text

	def create_label(self) -> Label:
		display_label = Label(text= self.label_text, size_hint= [1, .2],
						font_size= FONT_SIZE)
		return display_label

if __name__ == "__main__":
	TheApp().run()
