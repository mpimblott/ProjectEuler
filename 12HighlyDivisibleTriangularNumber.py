import math
import numpy as np


def generate_triangle(position):
    number = 0
    for n in range(position, 0, -1):
        number += n
    return number


def find_factors(number):
    no_factors = 0
    for i in range(1, math.trunc(math.sqrt(number))):
        if number % i == 0:
            no_factors += 2
    return no_factors


x = 1
while True:
    no = generate_triangle(x)
    f = find_factors(no)
    print(x)
    if f > 500:
        print('number found: ', no)
        break
    x += 1



