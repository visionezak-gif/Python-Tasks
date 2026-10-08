def minimum_numbers(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = umber
    return smallest
                

