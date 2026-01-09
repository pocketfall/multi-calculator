from kivy.app import App
from kivy.uix.label import Label
from components import ButtonGrid, MainLayout

class TheApp(App):
	def build(self):
		self.label_text = "hello i am a label"
		layout = self.create_layout()
		return layout

	def create_layout(self) -> MainLayout:
		layout = MainLayout()
		label = self.create_label()
		layout.add_widget(label)
		calculator_grid = self.create_calculator()
		layout.add_widget(calculator_grid)
		return layout
	
	def create_calculator(self) -> ButtonGrid:
		buttons = ButtonGrid(size_hint= [1, .8])
		return buttons

	def create_label(self) -> Label:
		display_label = Label(text= self.label_text, size_hint= [1, .2])
		return display_label

if __name__ == "__main__":
	TheApp().run()
