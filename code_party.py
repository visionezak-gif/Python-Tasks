#numbers = (23, 12, 11, 22,33, 44, ["boy"],55)
#
#numbers[6].append("9")
#	
#print(numbers)




#numbers = (1, 2, [3, 4], 5)
#
#new_list = list(numbers)
#
#new_list[2] = 99
#
#
#numbers = tuple(new_list)
#
#print(numbers)




#words = ('apple', 'banana', 'cherry')
#
#new_list = list(words)
#
#new_list.append("mango")
#
#print(new_list)
#
#new_tuple = tuple(new_list)
#
#print(new_tuple)



#
#numbers = (10, 20, 30, 40)
#
#first, second, *third = numbers
#print(first)
#print(second)
#print(third)



#for index in range(21):
#
#	def is_even(numbers):
#		if (numbers % 2 ==0):
#			return numbers
#			
#filtererd_list = filter(is_even, range(1, 21))
#print(list(filtererd_list))
#
#




#word = ['cat', 'elephant', 'tiger', 'lion']
#
#def get_length_greater_than_five(word):
#	return len(word) > 5
#	
#selected_word = list(map(get_length_greater_than_five, word))
#
#print(selected_word)




#THIS CODE DIDN'T WORK
#grade = [(1, 'A'), (4, 'B'), (2, 'C')]
#
#def values_greater_than_two(number):
#
#	for number in grade:
#
#		if number > 2:
#		
#			return number
#		
#		
#		
#new_result = (tuple(filter(values_greater_than_two, grade)))
#print(new_result)
#
#


#for index in range(51):
#
#	def is_divisible_by_3_and_5(numbers):
#		if (numbers % 3 ==0 and numbers % 5 ==0):
#			return numbers
#			
#filtererd_list = filter(is_even, range(1, 51))
#print(list(filtererd_list))
#




#words = ['level', 'world', 'madam', 'python']
#
#def is_palindrome(word):
#	return word == word[::-1]
#		
#
#
#filtered_list = list(filter(is_palindrome, words))
#print(filtered_list)




#words = ['python', 'java', 'c++']
#def upper_case_conversion(word):
#	return word.upper()
#	
#new_word = list(map(upper_case_conversion, words))
#
#print(new_word)




#def square_of_numbers(numbers):
#	return numbers * numbers
#
#
#result = list(map(square_of_numbers, range(1, 10)))
#print(result)






#name = ['john', 'mary', 'steve']
#def upper_case_conversion(word):
#	for index in name:
#		return word.upper()
#	
#result = list(map(upper_case_conversion, name[0]))
#print(result)




#from functools import reduce
#for index in range(1, 50):
#	def sum_up_score(accumulator, score):
#		
#		return accumulator + score
#	
#sum = reduce(sum_up_score, range(1, 50))
#print(sum)


from functools import reduce
integers = [3, 5, 9, 2, 8]

def largest_number(numbers):
	largest = 0
	for number in integers:
	
		if number > largest:
			
			return number
			
result = reduce(largest_number, integers)
print(result)




