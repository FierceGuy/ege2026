def game(hill_1,  move): 
    if hill_1  >=39 or move > 2: # если в куче более 65 камней или ход больше 2
        return move ==2 # должен быть первый ход Вани
    if move % 2 ==0: # если ход Пети, то при любом ходе Пети Ваня может выиграть своим первым ходом
        return all([game(hill_1 +1,  move+1),game(hill_1 +3,  move+1),game(hill_1 *2,  move+1)])
    return any([game(hill_1 +1,  move+1),game(hill_1 +3,  move+1),game(hill_1 *2,  move+1)])

for S in range(1, 39): # перебираем числа до 39
    if game(S, 0): # в первой куче камней S
        print(S)