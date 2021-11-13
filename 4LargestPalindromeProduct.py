import math

palindromes = []


def reverse(n):
    reverse_n = 0
    while n > 0:
        last_digit = n % 10
        reverse_n = (reverse_n * 10) + last_digit
        n = math.trunc(n / 10)
    return reverse_n


for i in range(100000, 999999):
    if i == reverse(i):
        palindromes.append(i)

for x in range(0, len(palindromes)):
    for z in range(100, 999):
        if palindromes[x] % z == 0 and 100 < (palindromes[x] / z) < 1000:
            print(palindromes[x])

