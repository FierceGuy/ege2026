def f(N):
    R = bin (N)[2:]
    for _ in range(2):
        sumd = R.count("1")
        R = R + str(sumd%2)
    