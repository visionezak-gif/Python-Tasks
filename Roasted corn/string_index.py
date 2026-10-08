def string_index(word):
	for index in word:
		if (index % 2 != 0):
			return word
	
word = "semicolon"

print(string_index(word))
		
