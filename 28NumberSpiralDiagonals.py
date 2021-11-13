import math
import sys
import numpy as np

size = 1001
point = 1
sum_total = 1

n = 2
while point < size**2:
    for i in range(1, 5):
        point += n
        sum_total += point
        print('point: ', point)
    n += 2
print('sum: ', sum_total)

