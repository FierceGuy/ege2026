print ('z w y x')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((y <= x) and (not (z)) and w)==1:
                    print(z, w , y ,x)