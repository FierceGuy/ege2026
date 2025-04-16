# Значение арифметического выражения 9**250 + 9**150 – х, где х – натуральное число, не превышающее 2000, 
# записали в системе счисления с основанием 9. Определите максимальное значение x, при котором данная запись 
# содержит наибольшее количество цифр «1».

def convert(number, system):
    result = ""
    while number != 0:
        result += str(number % system)
        number = number // system
    return result[::-1]

# print(convert(758, 10))

maxX = 0
max1 = 0
e = 9**250 + 9**150
for x in range(0, 2000+1):
    t = e - x 
    t = convert(t, 9)
    count1 = t.count("1")
    if count1 > max1:
        max1 = count1
        maxX = x
print(maxX)    