def x(z, v):
    if z <= 0 or v >3:
        return v ==3 and z == 0
    ng=[x(z-2,v+1), x(z-3,v+1), x(z//2,v+1)]
    if v % 2 == 1:
        return all (ng)
    return any (ng)

for s in range(0, 31):
    if x(s, 0):
        print (s)