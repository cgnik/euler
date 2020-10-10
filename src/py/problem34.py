# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.
# https://projecteuler.net/problem=34

from math import factorial
from time import process_time

# [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
facs = [factorial(x) if x > 0 else 0 for x in range(0, 10)]
facs_s = {str(x): factorial(x) if x > 0 else 1 for x in range(0, 10)}


def facs_sum_s(num):
    return sum([facs_s[c] for c in list(str(num))])


def facs_sum(num):
    n = num
    s = 0
    while n > 0:
        s += facs[n % 10]
        n = int(n / 10)
    return s


def find_answers():
    # '2540160' is the sum of factorial(9) for '9999999', at which point 9999999 exceeds the max
    # factorial sum for the digit length '7' and will continue to grow, so we can stop there,
    # as beyond that point, the sum of the factorials can never equal the number
    x = 3
    while x < 2540160:
        print(f"\rTesting {x:07d}", flush=True, end='')
        if facs_sum_s(x) == x:
            print(f"\r \u2713 {x:07d}", flush=True)
            yield x
        x = x + 1


def problem34():
    start = process_time()
    answers = []
    for a in find_answers():
        answers.append(a)
    print(f"\nProblem 34: {sum(answers)}, time: {process_time() - start}s answers: {answers}, facs: {facs}")
    # 40730


problem34()
