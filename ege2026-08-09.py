# можно просто сделать А=0, В = 1, Р = 2 вместо перевода в троичную систему счисления
def con(number, system):
    result =  ""
    while number > 0:
        result  += str(number % system)
        number = number // system
    return result[::-1]

ourlist = []
for n in range(3**7):
    r = con(n,3).zfill(7)

    if r.count('0') == 3 and r.count('1') == 2 and r.count('2') == 2:
        ourlist.append(r)

#АВР = 012

count = 1
#print(count, number[0],number.count('000'))
for number in ourlist:
    #print(count, number)
    if count % 2 == 0 and number[0] == '1' and number.count('000') == 1 and number.count('22') == 0:
        print(count, number)

    count += 1