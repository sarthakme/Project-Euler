num = 1000

#For co-prime numbers
a = 3
b = 5

p1 = (num - 1) // a
p2 = (num - 1) // b
p3 = (num - 1) // (a * b)

n1 = (p1 * (p1 + 1) * a) // 2
n2 = (p2 * (p2 + 1) * b) // 2
n3 = (p3 * (p3 + 1) * a * b) // 2

print(n1 + n2 - n3)

'''
For non-co-prime numbers
First find LCM

mx = max(a, b)
mn = min(a, b)

n = mx
while n <= mx * mn:
    if n % mn == 0:
        LCM = n
        break
    n += mx

Instead of a * b term, use LCM
'''
