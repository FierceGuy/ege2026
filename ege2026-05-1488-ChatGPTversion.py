# ЕГЭ №1716: разность между max и min двузначными числами из цифр N
# Учебный вариант с проверками и ясной логикой

def digits_sorted(n: int):
    """Возвращает отсортированные по возрастанию цифры трёхзначного числа n."""
    d = [n // 100, (n // 10) % 10, n % 10]
    d.sort()
    return d  # a <= b <= c

def diff_value(n: int) -> int:
    """Вычисляет разность max2 - min2 по правилам задачи с учётом запрета ведущего нуля."""
    a, b, c = digits_sorted(n)
    if a == 0:
        # max = 10*c + b, min = 10*b + 0 => diff = 10*c - 9*b
        return 10 * c - 9 * b
    else:
        # max = 10*c + b, min = 10*a + b => diff = 10*(c - a)
        return 10 * (c - a)

# Контрольные проверки (аналогично демонстрациям в полном файле)
assert diff_value(307) == 43  # max=73, min=30
assert diff_value(746) == 30  # max=76, min=46

# Подсчёт количества чисел на [900; 999] с разностью 70
count = sum(1 for N in range(900, 1000) if diff_value(N) == 70)
print(count)  # 15
