word  = input("Введите слово из латинских букв: ")
word_length = len(word)

if word_length % 2 != 0: 
    index = word_length // 2
    print(word[index])
else: 
	index_1 = word_length // 2 - 1
	index_2 = word_length // 2
	print(word[index_1:index_2 + 1])