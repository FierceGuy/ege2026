# Значение арифметического выражения 7400 + 7300 – х, где х – натуральное число, не превышающее 7400, 
# записали в системе счисления с основанием 7. Определите наибольшее количество нулей, которое может содержать 
# семиричная запись значения данного арифметического выражения.
def convert(number, system):
    result = ""
    while number != 0:
        result += str(number % system)
        number = number // system
    return result[::-1]

max0 = 0

cool = 7**400 + 7**300
for x in range(7**400, 0, -1):
    res = cool - x
    res = convert(res, 7)
    lol =  res.count('0')
    if lol > max0:
        max0 = lol
    print (lol)
    break