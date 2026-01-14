from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty
from components import ButtonGrid, MainLayout, Manager, InterfaceContainer
from config import BUTTONS, FONT_SIZE, LABEL_TEXT_SIZE, SCREENS

class TheApp(App):
	label_text_size = LABEL_TEXT_SIZE

	def build(self):
		self.title = "Calculator Maximum"
		self.label_text = "0"
		self.numbers = []
		self.layout = self.create_layout()
		return self.layout

	def create_layout(self) -> Manager:
		screen_manager = Manager()

		for screen_name in SCREENS:
			screen = InterfaceContainer(name= screen_name)
			screen_manager.add_widget(screen)
		screen_manager.current = SCREENS[0]
		return screen_manager	


if __name__ == "__main__":
	TheApp().run()
