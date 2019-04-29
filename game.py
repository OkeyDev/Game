import random
import os
RanNum = random.randint(0,1000)
while True:
	number = int(input("Напишите число \n"))
	if number == RanNum:
		os.system("echo -e '\e[1;32mВаu,YouWin!\e[0m'")
		break
	elif number > RanNum:
		os.system("echo -e '\e[1;33mСпускайся на тренді ютуба\e[0m'")
	elif number < RanNum:
		os.system("echo -e '\e[1;34mБольше\e[0m'")
print("Поздравляю, поздравлений нет!!!")
input("Нажмите на любую клавишу для продолжения");
