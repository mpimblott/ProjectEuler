prev_1 = 1
prev_2 = 1

count = 3
while True:
    next_term = prev_1 + prev_2
    print(next_term)
    if len(str(next_term)) == 1000:
        print(count)
        break
    # shift back
    prev_2 = prev_1
    prev_1 = next_term
    count += 1
