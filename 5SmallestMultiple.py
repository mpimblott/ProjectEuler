n = 40
while True:
    print(n)
    for x in range(11, 21):
        if n % x != 0:
            break
        elif n % x == 0 and x == 20:
            print('ANSWER FOUND' + str(n))
            quit()
    n += 20
