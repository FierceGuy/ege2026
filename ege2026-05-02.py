
def f(N):
    R = bin (N)[2:]
    for _ in range(2):
        sumd = R.count("1")
        R = R + str(sumd%2)
    return int(R, 2)

Rlist = []
for N in range (100):
    R = (f(N))
    if R > 123:
        Rlist.append(f(N))

print(min(Rlist))