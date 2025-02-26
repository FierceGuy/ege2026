def f (a, moves):
    n = len(moves)
    if n > 2 and moves[-3] == moves[-1]:
        return n % 2 != 1
    if a >= 21 or n > 3:
        return n == 3
    if n % 2 ==1:
        return all([f(a + 1, moves + [1]), f(a + 2, moves + [2]), f(a * 2, moves + [3])])
    return any([f(a + 1, moves + [1]), f(a + 2, moves + [2]), f(a * 2, moves + [3])])

for s in range(1, 20 + 1):
    if f(s, []):
        print(s)