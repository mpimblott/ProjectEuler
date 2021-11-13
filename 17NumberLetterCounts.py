import math

total_length = 0
word = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
        11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
        18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
        70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 0: 'Zero'}


def convert_number(n):
    name = ''
    length = len(str(n))
    if length == 4:
        name = 'OneThousand'
    elif length == 3:
        tens = n % 100
        if 9 < tens < 21:
            name = word[tens] + name
        elif tens < 10:
            name = word[tens] + name
        elif tens > 20:
            digits = n % 10
            tens = math.trunc((n % 100) / 10)
            tens = tens * 10
            if digits == 0:
                name = word[tens] + name
            else:
                name = word[tens] + word[digits] + name
        hundreds = math.trunc(n / 100)
        if tens == 0:
            name = word[hundreds] + 'Hundred'
        else:
            name = word[hundreds] + 'HundredAnd' + name
    elif length == 2:
        if 9 < n < 21:
            name = word[n] + name
        elif n > 20:
            digits = n % 10
            tens = n - digits
            if digits == 0:
                name = word[tens]
            else:
                name = word[tens] + word[digits]
    elif length == 1:
        name = word[n]
    return name


for i in range(1, 1001):
    print(convert_number(i))
    total_length += len(convert_number(i))
print(total_length)