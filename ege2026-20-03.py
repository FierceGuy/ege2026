def game(a,  move): 
    if a  >=39 or move > 3: # если в куче более 39 камней или ход больше 3
         return move ==3 # должен быть второй ход Пети
    if move % 2 ==1: # если ход Вани, то при любом ходе Вани Петя может выиграть своим вторым ходом
        return all([game(a +1,  move+1),game(a +3,  move+1),game(a *2,  move+1)])
    return any([game(a +1,  move+1),game(a +3,  move+1),game(a *2,  move+1)])

for S in range(1, 38+1): # перебираем числа до 39
    if game(S, 0): # в первой куче камней S
        print(S)