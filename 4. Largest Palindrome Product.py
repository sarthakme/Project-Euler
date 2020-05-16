mx = 0
b = 0
for i in range(999, 316, -1):
    f = 1
    if i % 11 == 0:
        k = i
        l = 100
        m = -1
    else:
        k = i - (i % 11)
        l = 109
        m = -11
    for j in range(k, l, m):
        mul = i * j
        if len(str(mul)) < 6 or mul <= mx:
            if f == 1:
                b = 1
                break
            break
        if str(mul) == str(mul)[::-1] and mul > mx:
            mx = mul
        f = 0
    if b == 1:
        break
print(mx)
