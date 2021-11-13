import math
import numpy as np
integers = []
lim = 2000000
total = 0


class Integer():
    def __init__(self, position, value=0, marked=False):
        self.position = position
        self.value = value
        self.marked = marked


def make_integer(position, value, marked):
    return Integer(position, value, marked)


for i in range(2, lim + 1):
    integers.append(make_integer(i-2, i, False))


for x in integers:
    multiple = 1
    pos = x.position
    val = x.value
    if not x.marked:
        while pos + (val * multiple) <= len(integers) - 1:
            integers[pos + x.value * multiple].marked = True
            multiple += 1


for x in integers:
    if not x.marked:
        total += x.value

print(total)




















