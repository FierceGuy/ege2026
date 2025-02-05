def transform(num):
    binary = bin(num)[2:]  # Получаем двоичное представление числа num
    if num % 2 == 0:
        result = "10" + binary
    else:
        result = "1" + binary + "01"
    return int(result, 2)

max_R = 0

for N in range(1, 13):  # Перебираем все числа от 1 до 12 включительно
    R = transform(N)
    if R > max_R:
        max_R = R

print(max_R)
