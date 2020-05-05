num = 1000
a = 3
b = 5
p1 = (num - 1) // a
p2 = (num - 1) // b
p3 = (num - 1) // (a * b)
n1 = (p1 * (p1 + 1) * a) // 2
n2 = (p2 * (p2 + 1) * b) // 2
n3 = (p3 * (p3 + 1) * a * b) // 2
print(n1 + n2 - n3)
