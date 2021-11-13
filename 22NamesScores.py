import math
import re
import numpy as np
from string import ascii_uppercase
from collections import OrderedDict

total_score = 0
alphabet = dict((ch, idx) for idx, ch in enumerate(ascii_uppercase, 1))
file = open('22names.txt', 'r')
text = file.read()
text = re.sub('["""]', '', text)
A = np.array(text.split(','))
A = np.sort(A)
print(A)
print(alphabet)
for n in range(0, len(A)):
    alphabet_score = 0
    name = A[n]
    for l in range(0, len(name)):
        alphabet_score += alphabet[name[l]]
    total_score += alphabet_score * (n + 1)
print(total_score)

