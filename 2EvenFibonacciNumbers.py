def fibonacci(lim):
    sequence = [1, 2]
    while True:
        next_term = sequence[-1] + sequence[-2]
        if next_term <= lim:
            sequence.append(next_term)
        else:
            break
    return sequence


def find_even_sum(sequence):
    total = 0
    for i in range(0, len(sequence)):
        if sequence[i] % 2 == 0:
            total += sequence[i]
    return total


print(find_even_sum(fibonacci(4000000)))




