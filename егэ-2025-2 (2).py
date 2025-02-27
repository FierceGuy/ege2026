print('w,z,y,x,F')

for x in [0, 1]:
    for y in range(0,2):
        for z in range(0, 2):
            for w in range(0, 2):
                #(x → (z ≡ w)) ˅ ¬(y → w)
                F = (x <= (z == w)) or not (y <= w)
                if F ==0:
                    print(w,z,y,x,F)