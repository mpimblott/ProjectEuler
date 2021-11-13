import math

primes = [1, 2, 3]
num = 5


def is_prime(n):
    for i in range(1, len(primes)):
        if primes[i] <= math.sqrt(n) and n % primes[i] == 0:
            return False
    return True


while len(primes) <= 10001:
    #print(len(primes))
    print(len(primes))
    if is_prime(num):
        primes.append(num)
    num += 2
print(primes)
print(primes[-1])

