import math
import numpy as np


class Sequence():
    def __init__(self, length, a, b):
        self.length = length
        self.a = a
        self.b = b


longest_sequence = Sequence(0, 0, 0)


def is_prime(n):
    if n < 0:
        return False
    elif all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)):
        return True
    else:
        return False


def sequence_length(a, b):
    n = 0
    while True:
        if is_prime(n**2 + a*n + b):
            n += 1
        else:
            return n+1


for a in range(-999, 1000):
    print('a: ', a)
    for b in range(-1000, 1001):
        length = sequence_length(a, b)
        if length > longest_sequence.length:
            longest_sequence = Sequence(length, a, b)


print('a: ', longest_sequence.a)
print('b: ', longest_sequence.b)
print('ab: ', longest_sequence.a * longest_sequence.b)
print('len: ', longest_sequence.length)



