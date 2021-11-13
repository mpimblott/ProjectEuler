import math
import numpy as np


def check(n):
    original = n
    total = 0
    for x in range(0, len(str(n))):
        last_digit = n % 10
        total += last_digit**5
        n //= 10
    if total == original:
        print('in set: ', original)

n = 0
while True:
    check(n)
    n += 1