letters = []

def checkstring(text,symbols):
	count = 0
	while count < len(text):
		if  text[count] not in symbols:
			return False
		count += 1
	return True

def checkforletters(string,printl,output,catalogue):
	count = 0
	stringtolist("ABCDEFGHIJKLMNOPQRSTUVWXYZ",catalogue)
	while count < len(string):
		sym = string[count]
		if sym in catalogue:
			sym = catalogue.index(sym, 0, len(catalogue)) + 10
		output.append(sym)
		count += 1
	if printl == 1:
		print(output)

def stringtolist(string,catalogue):
	count = 0
	while count < len(string):
		catalogue.append(string[count])
		count += 1

def intlist():
	count = 0
	while count < len(total):
		total[count] = int(total[count])
		count += 1

def convertdecimal(a,abase):
	count = 0
	count2 = len(a) - 1
	decimal = 0
	while count < len(a):
		decimal = decimal + a[count2] * (abase ** count)
		count += 1
		count2 -= 1
	return decimal

def converttoy(ybase,xdecimal,output):
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
	return(output)

def checklist(catalogue,llist):
	count = 0
	while count < len(catalogue):
		sym = catalogue[count]
		if sym > 9:
			sym = llist[sym - 10]
		catalogue[count] = sym
		count += 1
	return catalogue

def listtostring(catalogue):
	count = 0
	output = ""
	while count < len(catalogue):
		output = output + str(catalogue[count])
		count += 1
	return output

def addtext(text2):
	journal = open("journal.txt","a")
	journal.write(str(text2) + '\n')

def readtext():
	journal = open("journal.txt","r")
	content = journal.read()
	return content

def text(text):
	addtext(text)
	print(text)

print("|------------------- MENU -------------------|")
print("|Options: 1 - start converting.              |")
print("|         0 - exit.                          |")
print("|Developers:                                 |")
print("|           An_Idea - Maksim Gusev           |")
print("|All code is made personally.                |")
print("|Copying is allowed.                         |")
print("|--------------------------------------------|")
journal = open("journal.txt","a")
cont = readtext()
print(cont)

while True:
	total = []
	option = input("Enter your option: ")
	if option == "0" or option == None:
		break
	elif option == "1":
		x = input("Enter the number you want to convert: ")
		xbase = int(input("Enter the base of this number: "))
		ybase = int(input("Enter the base of the number you want to get: "))
		text("-" * 46)
		text("Your number: " + str(x) + " - with base " + str(xbase))
		if xbase > 37 or xbase < 2 or ybase > 37 or ybase < 2:
			print("You can convert numbers only with base less than 37 and bigger than 1. ")
		else:
			x = x.upper()
			if checkstring(x,"ABCDEFGHIJKLMNIOPQRSTUVWXYZ1234567890") == True:
				checkforletters(x,0,total,letters)
				intlist()
				decimal = convertdecimal(total,xbase)
				text("Decimal: ")
				text(decimal)
				total = converttoy(ybase,decimal,total)
				total = checklist(total,letters)
				answer = listtostring(total)
				text("Your answer is: ")
				text(answer)
				text("-" * 46)
			else:
				print("You have a mistake in the number\'s characters.")
	else:
		print("Incorrect option.")
journal.close()
