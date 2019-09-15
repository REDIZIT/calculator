letters = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def convert_to_decimal(a,abase):
	# a - строка, число которое переводим
	# abase - число, база a
	return int(a, abase)

def convert_to_y(ybase,xdecimal):
	# ybase - база числа, которое хотим получить на выходе
	# xdecimal - число, которое переводим - в десятичной системе счисления
	# ОБА АРГУМЕНТА - ЦЕЛЫЕ ЧИСЛА
	output = []
	num = xdecimal
	while True:
		if num < ybase:
			output.append(num)
			break
		else:
			output.append(num % ybase)
			num = num // ybase
	output.reverse()
	# checklist() проверяет, есть ли в списке output числа больше 9 и 
	# заменяет их буквенной записью, а также переводит все элементы списка
	# в строку
	checklist(output)
	# Переводим все элементы списка в строку
	output = "".join(output)
	return(output)

def checklist(catalog):
	for count in range(0, len(catalog)):
		sym = catalog[count]
		if sym > 9:
			sym = letters[sym]
		catalog[count] = str(sym)
	return catalog

number = 1000
print(convert_to_y(2, number))

number = "FA"
print(convert_to_decimal(number, 16))