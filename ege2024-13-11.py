def to_binary(num):
    return bin(num)[2:].zfill(8)

b1 = to_binary(136)
b2 = to_binary(151)
count = 1
for i, j in zip(b1, b2):
    if i == j:
        count += 1
        continue
    break
mask_min = f"{count * '1'}{"0"*(8-count)}"
print(int(mask_min, 2))
