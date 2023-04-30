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

	def convertRome(self):
		"""
		Перевод числа в римскую систему
		"""
		data = int(self.ids.number_input.text)
		ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
		tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
		hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
		thous = ["", "M", "MM", "MMM", "MMMM"]
		t = thous[data // 1000]
		h = hunds[data // 100 % 10]
		te = tens[data // 10 % 10]
		o = ones[data % 10]
		self.ids.result_main.text = "Результат: " + str(t + h + te + o)

	def convertMorse(self):
		"""
		Перевод в систему Морзе
		"""
		data = str(self.ids.number_input.text)
		morse = {'а': '.-',
		        '0': '-----',
		        '1': '.----',
		        '2': '..---',
		        '3': '...--',
		        '4': '....-',
		        '5': '.....',
		        '6': '-....',
		        '7': '--...',
		        '8': '---..',
		        '9': '----.'}
		result = []
		for element in data:
		    result.append(morse[element])
		self.ids.result_main.text = "Результат: " + ''.join(result)

	def convertMali(self):
		"""
		Перевод в систему Мали
		"""
		number = int(self.ids.number_input.text)
		part1 = number // 400
		part2 = (number - part1*400) // 80
		part3 = (number - part1*400 - part2*80) // 20
		part4 = (number - part1*400 - part2*80 - part3*20) // 10
		part5 = (number - part1*400 - part2*80 - part3*20 - part4*10) // 5
		part6 = (number - part1*400 - part2*80 - part3*20 - part4*10 - part5*5)
		res = f"{part1}*400+{part2}*80+{part3}*20+{part4}*10+{part5}*5+{part6}*1"
		self.ids.result_main.text = "Результат: " + res
	def convertAlambak(self):
		number = int(self.ids.number_input.text)
		res = f""
		part1 = number // 20
		part2 = (number - part1*20) // 10
		part3 = (number - part1*20 - part2*10) // 5
		part4 = (number - part1*20 - part2*10 - part3*5) // 2
		part5 = (number - part1*20 - part2*10 - part3*5 - part4*2)
		if part1 >0:
			res += f"{part1}*20"
		if part2 >0:
			res += f"+{part2}*10"
		if part3 >0:
			res += f"+{part3}*5"
		if part4 >0:
			res += f"+{part4}*2"
		if part5 >0:
			res += f"+{part5}*1"
		self.ids.result_main.text = "Результат: " + res

	def convertTsotsil(self):
		number = int(self.ids.number_input.text)
		res = f""
		part1 = number // 20
		part2 = (number - part1*20)
		if part1 > 0:
			res += f"{part1} человек "
		if part2 == 1:
			res += f"{part2} палец"
		if part2 >= 2 and part2 <= 4:
			res += f"{part2} пальца"
		if part2 >=5:
			res += f"{part2} пальцев"
		self.ids.result_main.text = "Результат: " + res

	def convertMaya(self):
		number = int(self.ids.number_input.text)
		res = f""
		part1 = number // 64000000 #Алавтун
		part2 = (number - part1*64000000) // 3200000 #Кинчильтун 
		part3 = (number - part1*64000000 - part2*3200000) // 160000 #Калабтун 
		part4 = (number - part1*64000000 - part2*3200000 - part3*160000) // 8000 #Пиктун 
		part5 = (number - part1*64000000 - part2*3200000 - part3*160000 - part4*8000) // 400 #Бактун
		part6 = (number - part1*64000000 - part2*3200000 - part3*160000 - part4*8000 - part5*400) // 20 #Катун
		part7 = (number - part1*64000000 - part2*3200000 - part3*160000 - part4*8000 - part5*400 - part6*20) // 1 #Тун
		if part1 >0:
			res += f"{part1} Алавтун "
		if part2 >0:
			res += f"{part2} Кинчильтун "
		if part3 >0:
			res += f"{part3} Калабтун "
		if part4 >0:
			res += f"{part4} Пиктун "
		if part5 >0:
			res += f"{part5} Бактун "
		if part6 >0:
			res += f"{part6} Катун "
		if part7 >0:
			res += f"{part5} Тун "
		self.ids.result_main.text = "Результат: " + res