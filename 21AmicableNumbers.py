import math
import math as np
amicable_total = 0


def sum_factors(number):
    total = 0
    for x in range(1, math.trunc(math.sqrt(number))):
        if number % x == 0:
            total += x
            total += number // x
    total -= number
    return total


for i in range(4, 9999):
    if i == sum_factors(sum_factors(i)) and i != sum_factors(i):
        print(i)
        amicable_total += i

print(sum_factors(28))
print(amicable_total)
