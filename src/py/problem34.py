# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.
# https://projecteuler.net/problem=34

from math import factorial
from time import process_time

facs = [factorial(x) if x > 0 else 0 for x in range(0, 10)]


def facs_sum(num):
    n = num
    s = 0
    while n % 10 == 0:
        n = int(n / 10)
    while n > 0:
        s += facs[n % 10]
        if s > num:
            return 0
        n = int(n / 10)
        while n > 0 and n % 10 == 0:
            n = int(n / 10)
    return s


def find_answers():
    # '2540160' is the sum of factorial(9) for '9999999',
    # at which point 9999999 exceeds the facs sum, and will continue to, so we can stop there
    for x in range(3, 9999999):
        print(f"\r{x:05d}", flush=True, end='')
        if facs_sum(x) == x:
            yield x


def find_answersx():
    x = 3
    while True:
        x = x + 1
        if facs_sum(x) == x:
            yield x


def problem34():
    start = process_time()
    answers = list(find_answers())
    answer = sum(answers)
    print(f"Problem 34: {answer}, time: {process_time() - start}s answers: {answers}, facs: {facs}")


problem34()
