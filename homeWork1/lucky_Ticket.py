number_ticket = input("Введите шестизначный номер билета: ")

sum_first = int(number_ticket[0]) + int(number_ticket[1]) + int(number_ticket[2])

sum_last = int(number_ticket[3]) + int(number_ticket[4]) + int(number_ticket[5])

if sum_first == sum_last:
	print("Счастливый билет")
else: 
	print("Несчастливый билет")