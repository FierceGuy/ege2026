#  Значение арифметического выражения 6**900 + 6**10 – х, где х – натуральное число, не превышающее 10000, 
# записали в системе счисления с основанием 6. Определите максимальное значение x, при котором данная
#  запись содержит одинаковое количество цифр «3» и «5».

def convert(number, system):
    result = ""
    while number != 0:
        result += str(number % system)
        number = number // system
    return result[::-1]

число = 6**900 + 6**10
for x in range(10000, 0, -1):
    res = число - x
    res = convert(res, 6)
    тройки =  res.count('3')
    пятёрки =  res.count('5')
    if тройки == пятёрки:
        print(x)
        break