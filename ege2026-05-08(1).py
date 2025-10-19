alphabet = "0123456789AB"  # Только для основания 12

def convert_to_base(number, system):
    result = ''
    while number != 0:
        result += alphabet[number % system]
        number //= system
    return result[::-1]

maxR = 0
bestN = 0

for n in range(143, 1000):  # Ограничим диапазон
    r = convert_to_base(n, 12)
    b = n % 12
    if b == 0:
        r += r[-3:]  # Дописываем последние 3 цифры
    else:
        r = convert_to_base(b * 3, 12) + r  # Дописываем остаток * 3 в начало

    # Преобразуем r из двенадцатеричной системы в десятичную
    R = int(r, 12)
    if R < 58000 and R > maxR:
        maxR = R
        bestN = n

print(bestN)