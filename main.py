from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import SlideTransition
from kivy.properties import StringProperty, NumericProperty, DictProperty
from components import ButtonGrid, MainLayout, Manager, InterfaceContainer, ScreenSwitchLeft, ScreenSwitchRight
from config import BUTTONS, FONT_SIZE, LABEL_TEXT_SIZE, SCREENS, SCREEN_BUTTON_COLORS

class TheApp(App):
	label_text_size = StringProperty(LABEL_TEXT_SIZE)
	font_size = NumericProperty(FONT_SIZE)
	colors = DictProperty(SCREEN_BUTTON_COLORS)

	def build(self):
		self.title = "Calculator Maximum"
		self.label_text = "0"
		self.numbers = []
		self.layout = self.create_layout()
		return self.layout

	def create_layout(self) -> Manager:
		screen_manager = Manager()
		screen_manager.transition = SlideTransition(direction= "right")

		for screen_name in SCREENS:
			screen = InterfaceContainer(name= screen_name)
			self.add_switch_buttons(screen_name, screen)
			screen_manager.add_widget(screen)
		screen_manager.current = SCREENS[2]
		return screen_manager	

	def add_switch_buttons(self, screen_name: str, parent: InterfaceContainer) -> None:
		switcher = None
		switcher1 = None
		match screen_name:
			case "left":
				switcher = ScreenSwitchRight()
			case "middle":
				switcher1 = ScreenSwitchLeft()
				switcher2 = ScreenSwitchRight()
			case "right":
				switcher = ScreenSwitchLeft()
		if switcher:
			parent.add_widget(switcher)
		elif switcher1:
			parent.add_widget(switcher1)
			parent.add_widget(switcher2)
	
	def switch_right(self) -> None:
		current_screen = self.find_current_screen()
		self.layout.transition.direction = "left"
		if current_screen == "middle":
			self.layout.current = "right"
		else:
			self.layout.current = "middle"
	
	def switch_left(self) -> None:
		current_screen = self.find_current_screen()
		self.layout.transition.direction = "right"
		if current_screen == "middle":
			self.layout.current = "left"
		else:
			self.layout.current = "middle"
	
	def find_current_screen(self) -> str:
		return self.layout.current

if __name__ == "__main__":
	TheApp().run()
