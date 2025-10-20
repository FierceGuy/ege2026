s = '123456'
print(s)
s = s[:s.find('4')+1]
print(s)

def con(number, system):
    result =  ""
    while number > 0:
        result  += str(number % system)
        number = number // system
    return result[::-1]


def big5(s):
    for digit in s:
        if digit<5:
            return False
    return True

count = 0
for n in range(8**6):
    r = con(n, 8)
    if r.count("4") == 2 and r.count("44") == 0:
        if big5(beetween4()):
            print()