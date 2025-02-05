print ('z w y x')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((w <= y) <= x) or not(z))==0:
                    print(z, w , y ,x)