import math
import numpy as np

n = 2 ** 1000
digits = np.array([int(i) for i in str(n)])
print(digits)
total = np.sum(digits)
print(total)
