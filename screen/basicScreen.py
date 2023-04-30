import kivy
from kivymd.uix.screen import MDScreen

class BasicScreen(MDScreen):
	"""
	Класс для страницы с стандартными, классическими преобразованиями
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

	def convert(self, index, number):
		"""
		Перевод числа в двоичную, восьмиричную, десятичную и шестнадцатиричную системы
		"""
		if number[:2] == '0b' or number[:2] == '0B':
			num = int(number[2:])
			if index == 1:
				self.ids.result_basic.text = ''
				self.ids.result_basic.text = "Результат: " + format(num, 'd')
			elif index == 2:
				onum = int(str(num), 2)
				onum = oct(onum)
				self.ids.result_basic.text = ''
				self.ids.result_basic.text = "Результат: " + onum[2:]
			elif index == 3:
				decnum = int(number[2:], 2)
				self.ids.result_basic.text = ''
				self.ids.result_basic.text = "Результат: " + str(decnum)
			else:
				hexnum = int(str(num), 2)
				hexnum = hex(hexnum)
				self.ids.result_basic.text = ''
				self.ids.result_basic.text = "Результат: " + hexnum[2:]
		elif number[:2] == '0o' or number[2:] == '0O':
			num = int(number[2:])
			if index == 1:
				bnum = int(str(num), 8)
				bnum = bin(bnum)
				self.ids.result_basic.text = ''
				self.ids.result_basic.text = "Результат: " + bnum[2:]
			elif index == 2:
				self.ids.result_basic.text = ''
				self.ids.result_basic.text = "Результат: " + format(num, 'd')
			elif index == 3:
				decnum = int(number[2:], 8)
				self.ids.result_basic.text = ''
				self.ids.result_basic.text = "Результат: " + str(decnum)
			else: 
				hexnum = int(str(num), 8)
				hexnum = hex(hexnum)
				self.ids.result_basic.text = ''
				self.ids.result_basic.text = "Результат: " + hexnum[2:]
		elif number[:2] == '0x' or number[2:] == '0X':
			if index == 1:
				res = "{0:08b}".format(int(number[2:], 16))
				self.ids.result_basic.text = ''
				self.ids.result_basic.text = "Результат: " + res
			elif index == 2:
				num = number[2:]
				res = oct(int(num, 16))
				self.ids.result_basic.text = ''
				self.ids.result_basic.text = "Результат: " + res[2:]
			elif index == 3:
				decnum = int(number, 16)
				self.ids.result_basic.text = ''
				self.ids.result_basic.text = "Результат: " + str(decnum)
			else: 
				self.ids.result_basic.text = ''
				self.ids.result_basic.text = "Результат: " + number[2:]
		else:
			if index == 1:
				res = bin(int(number))
				self.ids.result_basic.text = ''
				self.ids.result_basic.text = "Результат: " + res[2:]
			elif index == 2:
				res = oct(int(number))
				self.ids.result_basic.text = ''
				self.ids.result_basic.text = "Результат: " + res[2:]
			elif index == 3:
				self.ids.result_basic.text = ''
				self.ids.result_basic.text = "Результат: " + number
			else:
				res = hex(int(number))
				self.ids.result_basic.text = ''
				self.ids.result_basic.text = "Результат: " + res[2:]