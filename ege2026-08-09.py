def con(number, system):
    result =  []
    while number > 0:
        result.append(number % system)
        number = number // system
    return result[::-1]