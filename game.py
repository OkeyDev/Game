import random
RanNum = random.randint(0,1000)
while true:
	number = int(input("Напишите число"))
	if number == RanNum:
		print("ты угадал")
		break
	elif number > RanNum:
		print("спускай на тренды ютуба")
	elif number < RanNum:
		print("больше")
print("Поздравляю, поздравлений нет!!!")
input("Нажмите на любую клавишу для продолжения");
