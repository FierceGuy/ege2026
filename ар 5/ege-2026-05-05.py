def con(number, system):
    result =  ""
    while number > 0:
        result  += str(number % system)
        number = number // system
    return result[::-1]

print(con(10, 6))


