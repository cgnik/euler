# Problem 23
# https://projecteuler.net/problem=23
# Non-abundant sums
#
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import numpy as np
import itertools as it

from util.abundant import abundant_numbers, contains_sum_for

max_abundant = 28123


def problem23():
    print("Calculating abundants...")
    abundant = abundant_numbers(max_abundant)
    print("Calculating positive integers not a sum of abundant numbers...")
    non_sums = list(set([x for x in range(1, max_abundant) if not contains_sum_for(x, abundant) and x not in abundant]))
    non_sums.sort()
    print(f"All non-sums (sum {sum(non_sums)}, count {len(non_sums)}): {non_sums}")


problem23()
