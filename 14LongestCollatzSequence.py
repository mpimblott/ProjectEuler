import math
import numpy as np
longest = 0
number_longest = 0


def collatz(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        length += 1
    return length


for i in range(1, 1000000):
    print(i)
    l = collatz(i)
    if l > longest:
        longest = l
        number_longest = i

print('longest: ', number_longest)