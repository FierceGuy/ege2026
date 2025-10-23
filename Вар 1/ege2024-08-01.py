# alphabet = "0123456789ABCDEF"

def convert(number, system):
    result =  []
    while number > 0:
        result.append(number % system)
        number = number // system
    return result[::-1]

def test(number):

    d1 = number.count(7)
    d911 =  number.count(9) +  number.count(10) +  number.count(11)

    if d1 == 1 and d911 < 3:
        return True
    return False

count = 0
for n in range(12**5):
    if test(convert(n,12)):
        count+=1

print(count)