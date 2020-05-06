s = 0
n = 4000000
a = 0
b = 1
if a % 2 == 0:
    s += a
if b % 2 == 0:
    s += b
while a + b <= n:
    a, b = a + b, a
    if a % 2 == 0:
        s += a
print(s)
