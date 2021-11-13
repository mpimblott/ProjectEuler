import math
import numpy as np
abundant_numbers = []
sum_abundant = []


def sum_factors(number):
    total = 0
    for x in range(1, math.trunc(math.sqrt(number))+1):
        if number % x == 0:
            total += x
            total += number // x
    total -= number
    return total


for n in range(12, 28124):
    if sum_factors(n) > n:
        abundant_numbers.append(n)
print(abundant_numbers)
