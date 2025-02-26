def solve():
    n = 4
    while True:
        s = "1" + "8" * n
        ones = 1
        while "18" in s or "388" in s or "888" in s:
            if "18" in s:
                s = s.replace("18", "8", 1)
            elif "388" in s:
                s = s.replace("388", "81", 1)
                ones += 1
            elif "888" in s:
                s = s.replace("888", "3", 1)
        if s.count("1") == 3:
            print(n)
            return
        n += 1

solve()