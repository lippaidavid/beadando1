import math
def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, (int(math.sqrt(n)) + 1), 2): #(int(n ** 0.5))
        if n % i == 0:
            return False
    return True


def nth(n):
    count = 0
    i = 1
    while count < n:
        i += 1
        if isPrime(i):
            count += 1
    return i

print(nth(2))
print(nth(10001))
