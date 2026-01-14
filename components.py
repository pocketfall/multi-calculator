from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from config import BUTTONS, FONT_SIZE, LABEL_TEXT_SIZE, SCREENS

class Manager(ScreenManager):
	pass

class InterfaceContainer(Screen):
	pass

class ScreenSwitches(AnchorLayout):
	pass

class MainLayout(BoxLayout):
	label_text = StringProperty("0")
	screen_names = ListProperty(None)

	def add_to_display(self, button_object: Button) -> None:
		button_text = button_object.text
		if button_text != "=":
			match button_text:
				case "<":
					self.delete_character()
				case "AC":
					self.label_text = ""
				case "":
					pass
				case _:
					self.label_text = button_text if self.label_text == "0" else self.label_text + button_text
		else:
			try:
				self.do_math()
			except Exception as e:
				print(e)
				self.label_text = "Something broke, please try again"

	def delete_character(self) -> None:
		self.label_text = self.label_text[:-1]

	def do_math(self) -> None:
		# clear label text
		operation_string = self.label_text
		self.label_text = ""

		# extract numbers
		operation_list = list(operation_string)
		operation_dict = self.handle_operation_string(operation_list)
		numbers = self.get_numbers(operation_list, operation_dict)

		# sum numbers, we don't actually need all the operators
		output = sum(numbers)
		self.label_text = str(output)

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

class ButtonGrid(GridLayout):
	callback = ObjectProperty(None)
	label_text = StringProperty(None)

	def on_kv_post(self, base_widget) -> None:
		self.add_buttons()

	def add_buttons(self) -> None:
		for button_text in BUTTONS:
			button = Button(text= button_text,
				   font_size= FONT_SIZE)
			if self.callback and self.label_text:
				button.bind(on_press= self.callback)
			self.add_widget(button)

