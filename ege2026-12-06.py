def editor(n):
    # Начальная строка: 1 + n восьмерок
    s = '1' + '8' * n
    
    while '18' in s or '388' in s or '888' in s:
        if '18' in s:
            s = s.replace('18', '8', 1)
        elif '388' in s:
            s = s.replace('388', '81', 1)
        elif '888' in s:
            s = s.replace('888', '3', 1)
    
    return s.count('1')

# Ищем минимальное значение n
n = 4  # начинаем с минимального значения n > 3
while True:
    if editor(n) == 3:
        print(n)
        break
    n += 1
