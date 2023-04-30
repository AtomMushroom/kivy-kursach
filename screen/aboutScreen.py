import kivy
from kivymd.uix.screen import MDScreen
import webbrowser

class AboutScreen(MDScreen):
	"""
	Класс для страницы "О приложении"
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
		Открыть страницу "О приложении
		"""
		self.ids.nav_drawer.set_state("close")
		self.manager.current = 'about'

	def openSite(self, index):
		"""
		Открыть в браузере веб ресурсы организаций
		"""
		if index == 1:
			webbrowser.open("https://www.python.org/")
		elif index == 2:
			webbrowser.open("https://kivy.org/")
		else:
			webbrowser.open("https://kivymd.readthedocs.io/en/1.1.1/")