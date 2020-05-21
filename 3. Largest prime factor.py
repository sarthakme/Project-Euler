n = 600851475143

sqrt = int(pow(n, 1 / 2))
if sqrt % 2 == 0:
    sqrt -= 1
    
'''
Even numbers cannot be prime (except 2), so if 'sqrt' is even,
subtract one to get the next odd number
'''

two = 1
for i in range(sqrt, 2, -2):
    if n % i == 0:
        #If i is a multiple of n, check whether it is a prime number or not
        f = 0
        for j in range(2, int(pow(i, 1 / 2)) + 1):
            if i % j == 0:
                f = 1
                break
        if f == 0:
            two = 0
            print(i)
            break

'''
If none of the odd prime numbers were able to divide the number,
it must be that either the number is prime or it is an exponential power of 2
'''
        
if two == 1:
    if n % 2 == 0:
        print(2)
    else:
        print(n)
