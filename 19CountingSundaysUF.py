import math
import numpy as np

day = {'sunday': 7, 'monday': 6, 'tuesday': 5, 'wednesday': 4, 'thursday': 3, 'friday': 2, 'saturday': 8}
ivd = {v: k for k, v in day.items()}
month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_lengths_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Month():
    def __init__(self, length, start_day, end_day):
        self.length = length
        self.start_day = start_day
        self.end_day = end_day


def make_month(length, start_day, end_day='unknown'):
    return Month(length, start_day, end_day)


def last_day(month):
    n = month.length
    # first sunday
    n -= day[month.start_day]
    sundays = n // 7
    n -= sundays * 7
    return ivd[8-n]


def first_day(last_month):
    n = day[last_month.end_day] - 1
    d = ivd[n]
    return d


def count_sundays(start_year, end_year):
    sundays_on_first = 0
    prev_month = make_month(31, 'friday')
    prev_month.end_day = last_day(prev_month)
    for y in range(start_year, end_year):
        if y % 4 != 0 or y == 1900:
            for m in month_lengths:
                print(m)
                current_month = make_month(m, first_day(prev_month))
                current_month.end_day = last_day(current_month)
                if current_month.start_day == 'sunday':
                    sundays_on_first += 1
                prev_month = current_month
        else:
            for m in month_lengths_leap:
                current_month = make_month(m, first_day(prev_month))
                current_month.end_day = last_day(current_month)
                if current_month.start_day == 'sunday':
                    sundays_on_first += 1
                prev_month = current_month
    return sundays_on_first


print(count_sundays(1900, 2001))
