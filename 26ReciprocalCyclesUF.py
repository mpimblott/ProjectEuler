import math
import numpy as np


def reciprocal(n):
    if n > 0:
        return np.float64(1/n)


for i in range(2, 999):
    print(reciprocal(i))
