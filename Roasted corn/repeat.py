def repeated(word, number):
    if type(number) == float:
        return word
        
    result = ""
    for index in range(number):
        result += word
    return result

