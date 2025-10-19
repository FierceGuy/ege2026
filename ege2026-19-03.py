def game(hill, ball):
    if hill >=39 or ball > 2:
        return ball ==2
    if ball % 2 == 0:
        return all([game(hill+1, ball +1), game(hill+3, ball +1), game(hill*3, ball +1)])
    return any([game(hill+1, ball +1), game(hill+3, ball +1), game(hill*3, ball +1)])


for s in range(0, 38+1):
    if game(s, 0):
        print(s)