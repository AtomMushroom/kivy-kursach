import kivy
from kivymd.uix.screen import MDScreen

class MainScreen(MDScreen):
	"""
	Класс для главной страницы приложения
	"""
	def openMainScreen(self):
		"""
		Открыть главную страницу
		"""
		self.ids.nav_drawer.set_state("close")
		self.manager.current = 'main'

	def openBasic(self):
		"""
		Открыть страницу стандартных преобразований
		"""
		self.ids.nav_drawer.set_state("close")
		self.manager.current = 'basic'

	def openAbout(self):
		"""
		Открыть страницу "О приложении"
		"""
		self.ids.nav_drawer.set_state("close")
		self.manager.current = 'about'