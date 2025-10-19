def game(a, b, n):
    if a+b >=227 or n >2:
        return n ==2
    ng = ([game(a+1, b, n+1), game(a*2, b, n+1), game(a, b+1, n+1), game(a, b*2, n+1)])
    if n % 2 == 0:
        return any (ng)
    return any (ng)

for s in range(0, 210):
    if game(17, s, 0):
        print(s)