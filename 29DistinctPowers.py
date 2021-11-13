import math
import numpy as np
n = []

for a in range(2, 101):
    for b in range(2, 101):
        x = a ** b
        print(x)
        n.append(x)

y = dict.fromkeys(n)
z = list(y)
print('len: ', len(z))
