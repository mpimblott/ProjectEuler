import math
import numpy as np


def fact(n):
    answer = n
    for i in range(1, n):
        answer *= (n-i)
    return answer


def sum_digits(n):
    print('summing: ', n)
    total = 0
    while n > 0:
        last_digit = n % 10
        print(last_digit)
        n //= 10
        total += last_digit
    return total


factorial = fact(100)
print(sum_digits(factorial))
