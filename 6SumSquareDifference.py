def sum_of_squares():
    total = 0
    for x in range(1, 101):
        total += x ** 2
    return total


def square_of_sum():
    total = 0
    for x in range(1, 101):
        total += x
    return total ** 2


print(square_of_sum() - sum_of_squares())
