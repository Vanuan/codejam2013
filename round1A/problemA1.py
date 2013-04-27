import math
from decimal import *
getcontext().prec = 50

def solve(a, b, c):
    delta = Decimal(b*b) - 4*a*c
    if delta < 0:
        raise "Ouch"
    c1 = ((b * -1) + Decimal.sqrt(delta)) / (2*a)
    c2 = ((b * -1) - Decimal.sqrt(delta)) / (2*a)
    return max(c1, c2)

def process_case(r0, volume_left):
    solution = long(solve(2, Decimal(2*r0-1), Decimal(-volume_left)))
    return solution

def read_input():
    r0, volume = map(long, raw_input().split())
    return r0, volume


def process_input():
    number_of_cases = int(raw_input())
    for case_number in range(1, number_of_cases + 1):
        r0, volume = read_input()
        answer = process_case(r0, volume)
        print 'Case #%d: %s' % (case_number, answer)


if __name__ == '__main__':
    process_input()
