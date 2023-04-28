from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (480, 853) #Размер окна, в 2,25 раз меньше, чем 1080*1920 

class ConvertApp(MDApp): #Базовый класс
	def build(self):
		self.title = "Нестандартный конвертер чисел"
		self.sm = ScreenManager()
		self.sm.add_widget(MainScreen(name='main'))
		self.theme_cls.theme_style = 'Dark'

		return self.sm

class MainScreen(Screen):
	pass

if __name__ == '__main__':
    ConvertApp().run()