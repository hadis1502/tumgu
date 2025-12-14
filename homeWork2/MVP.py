boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']



girls.sort()
boys.sort()

if len(boys) == len(girls):  
	girls.sort()
	boys.sort()
	print("Идеальные пары:")
	for n in range(len(boys)):
		print(boys[n], "и", girls[n])
else:  
    print("Внимание, кто-то может остаться без пары.")
