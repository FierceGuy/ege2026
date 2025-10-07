print(sum((lambda a,b,c: (c-a)*10 if a else 10*c-9*b)
          (*sorted(map(int, str(N)))) == 70
          for N in range(900,1000)))
