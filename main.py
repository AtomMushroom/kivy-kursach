from kivymd.app import MDApp

from kivy.lang import Builder
Builder.load_file('Convert.kv')

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

#Импорты экранов (страниц)
from screen.mainScreen import MainScreen
from screen.basicScreen import BasicScreen
from screen.aboutScreen import AboutScreen

Window.size = (480, 853) #Размер окна, в 2,25 раз меньше, чем 1080*1920 

class ConvertApp(MDApp): #Базовый класс
	def build(self):
		self.title = "Нестандартный конвертер чисел"
		self.sm = ScreenManager()
		self.mainScreen = MainScreen(name='main')
		self.basicScreen = BasicScreen(name='basic')
		self.aboutScreen = AboutScreen(name='about')

		self.sm.add_widget(self.mainScreen)
		self.sm.add_widget(self.basicScreen)
		self.sm.add_widget(self.aboutScreen)

		self.theme_cls.theme_style = 'Dark'

		return self.sm

if __name__ == '__main__':
    ConvertApp().run()