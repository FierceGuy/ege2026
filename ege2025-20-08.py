def g(a,n):
    if a >=20 or n >3:
        return n ==3 and a <= 26
    ng=([g(a+4,n+1), g(a*2,n+1)])
    if n % 2 ==1:
        return all (ng)
    return any (ng)

print (min([s for s in range(0, 20) if g(s, 0)]))
print (max([s for s in range(0, 20) if g(s, 0)])) 
#ahhahah