import os
import random
def NormalLevel():
	randomNum = random.randint(0,1000)
	while True:
		number = int(input("Введите колво подписчиков на канале, от 0 до 1000 \n"))
		if number == randomNum:
			os.system("echo -e '\e[1;37mПоздравляю, ты угадал\e[0m'")
			break
		elif number > randomNum:
			os.system("echo -e '\e[1;33mСпускайся на тренді ютуба'")
		else:
			os.system("echo -e '\e[1;34mПоднимайся віше гор'")
def HardLevel():
	randomNum = random.uniform(0.00,100.00)
	while True:
		number = float(input("Введите колво подписчиков на канале, от 0.00 до 100.00 \n"))
		print (randomNum)
		if number == randomNum:
			os.system("echo -e '\e[1;37mПоздравляю, ты угадал\e[0m'")
			break
		elif number > randomNum:
			os.system("echo -e '\e[1;33mСпускайся на тренді ютуба'")
		else:
			os.system("echo -e '\e[1;34mПоднимайся віше гор'")

def VeryHardLevel():
	while True:
		randomNum = random.randint(0,100)
		number = float(input("Введите колво подписчиков на канале, от 0 до 100 \n"))
		if number == randomNum:
			os.system("echo -e '\e[1;37mПоздравляю, ты угадал\e[0m'")
			break
		else:
			os.system("echo -e '\e[1;34mНе угадал,число изменилось'")
	
def GetLevel(Level):
	for i in Level:
		print(str(Level[i][1]) + ". " + i)
	Choose =int(input("Выберите режим> ")) 
	for i in Level:
		if Level[i][1] == Choose:
			Level[i][0]()

def StartGameFunc():
	GetLevel({"Нормально" : [NormalLevel,1],"Сложно(не работае)" : [HardLevel,2],"Экстрим" : [VeryHardLevel,3]})

def Exit():
	print("Нажмите ctrl + c")

def Menu(function):
	while True:
		number = 1
		for i in function:
			print(str(number) +". " + function[i][1])
			function[i].insert(2,number)
			number += 1
		try:
			Choose =int(input("Выберите действие> "))
		except ValueError:
			os.system(" echo -e '\e[31mЯ СКАЗАЛ ВВЕСТИ ЦИФРУ!!!\e[0m'")
		else:
			for i in function:
				if function[i][2] == Choose:
					function[i][0]()


Menu({"Start Game" : [StartGameFunc,"Начать игру"],"Exit" : [Exit,"Выйти"]})

