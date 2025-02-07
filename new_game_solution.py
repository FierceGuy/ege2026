def check_win(S):
    # Если S нечётное
    if S % 2 == 1:
        first_move = 3 * S
        if first_move >= 51:  # Нельзя выиграть первым ходом
            return False
        vanyas_move = 3 * first_move
        if vanyas_move >= 51:  # Ваня не должен выиграть своим ходом
            return False
        return 3 * vanyas_move >= 51  # Проверяем, выиграет ли Петя вторым ходом
    else:
        # Для чётного S проверяем ходы +1 и +3
        for add in [1, 3]:
            first_move = S + add
            if first_move >= 51:  # Пропускаем ходы, ведущие к немедленному выигрышу
                continue
            if first_move % 2 == 1:  # Проверяем только нечётные числа
                vanyas_move = 3 * first_move
                if vanyas_move < 51 and 3 * vanyas_move >= 51:
                    return True
        return False

# Находим все подходящие значения S
results = []
for S in range(1, 51):
    if check_win(S):
        results.append(S)

# Выводим два наибольших значения
if len(results) >= 2:
    print(sorted(results)[-2:])
