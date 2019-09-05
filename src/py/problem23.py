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

from util.cartesian import cartesian_product, all_factors

max_abundant = 28123 + 1

def problem23():
    abundants = []
    with open("abundants.txt") as f:
        abundants = list(map(int, f.read().strip().split(',')))
    if len(abundants) == 0:
        abundants = abundant_numbers(max_abundant)
        with open("abundants.txt", "w") as f:
            f.write(','.join(abundants))
    print(f"abundants ({len(abundants)}): {abundants}")
    all_nums = set(range(1, max_abundant))
    all_sums = set([x[0] + x[1] for x in it.product(np.array(abundants), np.array(abundants))])
    all_sums = set(filter(lambda x: x <= max_abundant, all_sums))
    print(f"all sums ({len(all_sums)} {max(all_sums)}): {all_sums}")
    all_diff = {e for e in all_nums if e not in all_sums and e not in abundants}
    print(f"all diff (sum {sum(all_diff)}, {max(all_diff)}): {all_diff}")


problem23()
