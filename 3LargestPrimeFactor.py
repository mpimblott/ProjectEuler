import math

n = 600851475143


def prime_factors(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num /= 2
    # now num is odd
    for i in range(3, math.trunc(math.sqrt(num))):
        if num % i == 0:
            factors.append(i)
            num /= i
        else:
            i += 2
    return factors


print(prime_factors(n))

