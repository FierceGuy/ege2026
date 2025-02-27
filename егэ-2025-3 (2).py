print('w,x,y,z,F')

for x in [0, 1]:
    for y in range(0,2):
        for z in range(0, 2):
            for w in range(0, 2):
                #(x → (z ≡ w)) ˅ ¬(y → w)
                F = (y <= x) and  not z and w
                if F ==1:
                    print(w,x,y,z,F)