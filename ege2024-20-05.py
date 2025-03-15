def game(hill_1, hill_2, move): 
    if hill_1 + hill_2 >=65 or move > 3: # если в двух кучах более 65 камней или ход больше 3
         return move ==3 # должен быть второй ход Пети
    if move % 2 == 1:
        return all([game(hill_1 +1, hill_2, move+1),game(hill_1 *3, hill_2, move+1),game(hill_1, hill_2+1, move+1),game(hill_1, hill_2*3, move+1)])
    return any([game(hill_1 +1, hill_2, move+1),game(hill_1 *3, hill_2, move+1),game(hill_1, hill_2+1, move+1),game(hill_1, hill_2*3, move+1)])


for S in range(0, 58): # перебираем числа до 58
    if game(6, S, 0): # в первой куче 6 камней, во второй S
        print(S)