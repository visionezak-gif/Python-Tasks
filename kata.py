#number = int (input("Enter a number: "))

#def is_prime (number)
#	if (number % 2 ==0)
	
#	return true


def subtraction_of_numbers (first_number, second_number):
	
	sum_of_nummbers = first_number - second_number
	
	if second_number ==0:
	
		return 0
	
	return sum_of_nummbers	
	
	
def divisio_of_numbers (first_number, second_number):
	
	sum_of_nummbers = first_number / second_number
	
	return sum_of_nummbers	
	
	
def factor_of_number (number):
	count = 0
	
	for index in range(1, number+1):
		if number % index == 0:
	  
			count= count + 1
	
	return count
	
	
def squar_of_number (number):
	
	
	for index in range(1, number+1):
		if index * index == number:
	
			return True
	
	
def is_palindrome(number):
	formal = number
	reverse_number = 0
	
	while number >0:
		sum_digit = number % 10
		reverse_number = reverse_number * 10 + sum_digit
		number = number // 10
	
	return formal == reverse_number
	
	
def factorial_of(number):
	factorial = 1
	
	for index in range(number, 0, -1):
		factorial = factorial * index
	
	return factorial
	
	
def square_of(number):
		
	return number * number
	

result_seven = square_of(5) 
print (result_seven)		
	
	
	
result_six = factorial_of(5) 
print (result_six)		
		
	
	
	


result_five = is_palindrome(51415) 
print (result_five)		
	

	
	
	
	
result_four = squar_of_number(25) 
print (result_four)		

	
	
	
	
	
result_three = factor_of_number(10) 
print (result_three)		

	
	
	
	
	
result_two = divisio_of_numbers(70, 2) 
print (result_two)		
	
	
	
result = subtraction_of_numbers(70, 45) 
print (result)	
	

