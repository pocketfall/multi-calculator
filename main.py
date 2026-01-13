from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from components import ButtonGrid, MainLayout
from config import BUTTONS, FONT_SIZE, LABEL_TEXT_SIZE

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
		buttons = ButtonGrid(self.add_to_display)
		return buttons

	def add_to_display(self, button_object: Button):
		button_text = button_object.text
		if button_text != "=":
			match button_text:
				case "BORRAR":
					self.delete_character()
				case "AC":
					self.label.text = ""
				case "":
					pass
				case _:
					self.label.text = button_text if self.label.text == "0" else self.label.text + button_text
		else:
			try:
				self.do_math()
			except Exception as e:
				print(e)
				self.label.text = "Something broke, please try again"
	
	def do_math(self) -> None:
		# clear label text
		self.label_text = self.label.text
		self.label.text = ""

		# extract numbers
		operation_list = list(self.label_text)
		operation_dict = self.handle_operation_string(operation_list)
		numbers = self.get_numbers(operation_list, operation_dict)

		# sum numbers, we don't actually need all the operators
		output = sum(numbers)
		self.label.text = str(output)

	def get_numbers(self, string_list: list[str], operation_dict: dict) -> list:
		numbers = []
		previous_key = list(operation_dict.keys())[0]
		# if there is only one operator the for loop, it ends prematurely so handle that
		if len(list(operation_dict.keys())) < 2:
			number1 = "".join(string_list[:previous_key])
			number2 = "".join(string_list[previous_key + 1:])
			numbers.append(int(number1))
			numbers.append(int(number2))
			return numbers
		for key, value in operation_dict.items():
			if len(numbers) < 1:
				number = "".join(string_list[:key])
			else:
				if list(operation_dict.keys())[-1] == key:
					# i do not like this repeated code :(
					number1 = "".join(string_list[previous_key + 1:key])
					number2 = "".join(string_list[key + 1:])
					numbers.append(int(number1))
					numbers.append(int(number2))
					return numbers
				else:
					number = "".join(string_list[previous_key + 1:key])
			numbers.append(int(number))
			previous_key = key
		return numbers

	def handle_operation_string(self, operation_list: list[str]) -> dict:
		operation = {}
		for idx, character in enumerate(operation_list):
			try:
				int(character)
			except:
				operation[idx] = character
		return operation
	
	def delete_character(self) -> None:
		self.label_text = self.label.text[:-1]
		self.label.text = self.label_text

	def create_label(self) -> Label:
		display_label = Label(text= self.label_text, size_hint= [1, .33],
						font_size= LABEL_TEXT_SIZE)
		return display_label

if __name__ == "__main__":
	TheApp().run()
