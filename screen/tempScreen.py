import kivy
from kivymd.uix.screen import MDScreen

class TempScreen(MDScreen):
	"""
	Класс для страницы температур
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

	def openTemp(self):
		"""
		Открыть страницу "Температура"
		"""
		self.ids.nav_drawer.set_state("close")
		self.manager.current = 'temp'

	def openAbout(self):
		"""
		Открыть страницу "О приложении"
		"""
		self.ids.nav_drawer.set_state("close")
		self.manager.current = 'about'

	def convertTemp(self):
		data = int(self.ids.temp_input.text) #градусы Цельсия °C
		fahrenheit_temp = data * 1.8 + 32 #градусы Фаренгейта °F
		kelvin_temp = data + 273.15 #градусы Кельвина K
		rankine_temp = fahrenheit_temp + 459.67 #градусы Ранкина °Ra
		reaumur_temp = data * 0.8 #градусы Реюмора °Re
		newton_temp = data * 0.33 #градусы Ньютона °N
		romer_temp = (data * 0.525) + 7.5 #градусы Рёмера °Ro
		delisle_temp = (100 - data) * 1.5 #градусы Делиля °De

		self.ids.fahrenheit_temp.text = "Шкала Фаренгейта: " + str(round(fahrenheit_temp, 2)) + " °F"
		self.ids.kelvin_temp.text = "Шкала Кельвина: " + str(round(kelvin_temp, 2)) + "K"
		self.ids.rankine_temp.text = "Шкала Ранкина: " + str(round(rankine_temp, 2)) + " °Ra"
		self.ids.reaumur_temp.text = "Шкала Реюмора: " + str(round(reaumur_temp, 2)) + " °Re"
		self.ids.newton_temp.text = "Шкала Ньютона: " + str(round(newton_temp,2 )) + " °N"
		self.ids.romer_temp.text = "Шкала Рёмера: " + str(round(romer_temp, 2)) + " °Ro"
		self.ids.delisle_temp.text = "Шкала Делиля: " + str(round(delisle_temp, 2)) + " °De"