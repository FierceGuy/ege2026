print ("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((y <= (not(x <= z))) or w)
                if F == 0:
                    print(x, y, z, w)