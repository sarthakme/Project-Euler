i = 3
j = 1
n = 10001
while j != n:
    f = 0
    for k in range(3, int(i ** (1 / 2)) + 1):
        if i % k == 0:
            f = 1
            break
    if f == 0:
        j += 1
    i += 2
print(i - 2)
