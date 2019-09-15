letters = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def checkstring(text):
	for i in text:
		if not i in letters:
			return False
	return True


def convert_to_decimal(a,abase):
	return int(a, abase)

def convert_to_y(ybase,xdecimal):
	# ybase - база числа, которое хотим получить на выходе
	# xdecimal - число, которое переводим - в десятичной системе счисления
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
	checklist(output)
	# Переводим все элементы списка в строки
	# Сливаем элементы списка в строку, сохраняем в output
	output = "".join(output)
	return(output)

def checklist(catalog):
	for count in range(0, len(catalog)):
		sym = catalog[count]
		if sym > 9:
			sym = letters[sym]
		catalog[count] = str(sym)
	return catalog

number = "z"
print(convert_to_y(16, 250))
