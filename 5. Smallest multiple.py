mul = 1
n = 20
l = list(range(2, n + 1))
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[j] % l[i] == 0:
            l[j] /= l[i]
    mul *= l[i]
print(mul)
