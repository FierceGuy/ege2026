def game(hill_1,  move): 
    if hill_1  >=39 or move > 4: # если в кучe более 39 камней или ход больше 4
         return move ==4 or move ==2 # должен быть второй или первый ход Вани
    if move % 2 ==0: # если ход Вани, то при любом ходе Вани Петя может выиграть своим вторым ходом
        return all([game(hill_1 +1,  move+1),game(hill_1 +3,  move+1),game(hill_1 *2,  move+1)])
    return any([game(hill_1 +1,  move+1),game(hill_1 +3,  move+1),game(hill_1 *2,  move+1)])

for S in range(1, 38+1): # перебираем числа до 39
    if game(S, 0): # в первой куче камней S
        print(S)