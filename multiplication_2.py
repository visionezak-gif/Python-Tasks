print ("Multiplication Table")



print('\t', end="  ")
	
	
character = """
   1  2  3  4  5  6  7  8  9
--------------------------------------
	|
	|
	|
	|
	|
	|
	|
	|
	|
"""
print (character)
		
for index in range (1, 10):
	for count in range(1, 10):
		print (index)
		print ((count * index), end='\t')
	

