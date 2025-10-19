# def game(h,  m): 
#     if h  >=51 or m > 3: # если в кучe более 39 камней или ход больше 3
#          return m ==3 # должен быть второй ход Пети
    
#     if m % 2 ==1: # если ход Вани, то при любом ходе Вани Петя может выиграть своим вторым ходом
#         if h % 2 == 0 and m > 0:
#             p_moves = [game(h +1,  m+1),game(h +3,  m+1)]
#         else:
#             p_moves = [game(h *3,  m+1)]

#         return all (p_moves)
#     return any(p_moves)

# for S in range(1, 50): # перебираем числа до 39
#     if game(S, 0): # в первой куче камней S
#         print(S)

def can_win(s, turn, memo):
    if s >= 51:
        return turn % 2 == 1  # Петя выигрывает, если ход нечетный (его ход)
    
    if (s, turn) in memo:
        return memo[(s, turn)]
    
    next_turn = turn + 1
    possible_moves = [s * 3, s + 1, s + 3]
    possible_moves = [move for move in possible_moves if move % 2 == 1]
    
    if turn % 2 == 1:  # Ход Пети
        result = any(can_win(move, next_turn, memo) for move in possible_moves)
    else:  # Ход Вани
        result = all(can_win(move, next_turn, memo) for move in possible_moves)
    
    memo[(s, turn)] = result
    return result

def find_values():
    memo = {}
    results = []
    for s in range(1, 51):
        if not can_win(s, 1, memo) and can_win(s, 2, memo):
            results.append(s)
    return sorted(results)[-2:]

print(find_values())