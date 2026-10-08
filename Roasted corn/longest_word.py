

#	return word["Semicolon", "boy", "girls", "BMW", "rangerovers"]
#longest = len("Semicolon")

#if len("boy") > longest:
#	longest = "boy"

	
#if len("girls") > longest:
#	longest = "girls"

#if len("BMW") > longest:
#	longest = "BMW"

#if len("rangerovers") > longest:
#	longest = "rangerovers"

#	print(longest_word(longest))

#longest_word = words[0]
def longest_word(words):	
	longest = words[0]


	
	for word in words:
		if len(word) > len(longest):
			longest = word
	
	return longest
		
words = ["Semicolon", "boy", "girls", "BMW", "rangerovers"]
	
print(longest_word(words))
	
		
