year = int(input("Введите номер года: "))

if year % 4 == 0:
	if (year % 100 == 0) & (year % 400 != 0):
		print("Обычный год")
	else:
		print("Високосный год")
else: 
	print("Обычный год")