from kivymd.app import MDApp

from kivy.lang import Builder
Builder.load_file('Convert.kv')

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

#Импорты экранов (страниц)
from screen.mainScreen import MainScreen
from screen.basicScreen import BasicScreen
from screen.tempScreen import TempScreen
from screen.aboutScreen import AboutScreen

#Window.size = (480, 853) #Размер окна, в 2,25 раз меньше, чем 1080*1920

Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'} #Анимация клавиатуры
Window.softinput_mode = "below_target"

class ConvertApp(MDApp): #Базовый класс
	def build(self):
		self.title = "Нестандартный конвертер чисел"
		self.sm = ScreenManager()
		self.mainScreen = MainScreen(name='main')
		self.basicScreen = BasicScreen(name='basic')
		self.tempScreen = TempScreen(name='temp')
		self.aboutScreen = AboutScreen(name='about')

		self.sm.add_widget(self.mainScreen)
		self.sm.add_widget(self.basicScreen)
		self.sm.add_widget(self.tempScreen)
		self.sm.add_widget(self.aboutScreen)

		self.theme_cls.theme_style = 'Dark'
		self.theme_cls.primary_palette = "Blue"


		return self.sm
	def switchThemeStyle(self):
		self.theme_cls.primary_palette = ("Blue" if self.theme_cls.primary_palette == "Red" else "Red")
		self.theme_cls.theme_style = ("Dark" if self.theme_cls.theme_style == "Light" else "Light")

if __name__ == '__main__':
    ConvertApp().run()
