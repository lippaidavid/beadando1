import math

def primeFactors(n):
    factors=[]
    while (n % 2 == 0):
        factors.append(2),
        n /= 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while(n%i == 0):
            factors.append(i),
            n /= i
    if n>2:
        factors.append(n)
    return factors

print(primeFactors(13195))
print(primeFactors(600851475143))