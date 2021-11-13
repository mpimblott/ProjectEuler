import math
import numpy as np
import itertools
import functools
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutations = []


def convert(list):
    # multiply each integer element with its
    # corresponding power and perform summation
    res = functools.reduce(lambda total, d: 10 * total + d, list, 0)
    return res


for i in itertools.permutations(digits):
    permutations.append(convert(i))
permutations = np.array(permutations)
permutations = np.sort(permutations)
print(permutations[999999])


