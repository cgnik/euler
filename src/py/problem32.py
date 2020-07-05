# https://projecteuler.net/problem=32
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
import util.permutation as p

numbers = "123456789"


def is_pandigital(x, c, p):
    s = list('{}{}{}'.format(x, c, p))
    s.sort()
    return ''.join(s) == numbers


def make_ints(charrays):
    for a in charrays:
        yield int(''.join(a))


def problem32():
    # strategy: brute force: permutations of "123456789"
    # broken into 3 strings
    # strings for the multiplicands must be 1-4 characters, each, no more,
    # considering that the use of 5 characters on the left of = would
    # necessitate the presence of no more than 4 on the right, which could
    # only be true if it was something like 2*4-digit=other-4-digit
    # this is like a 5 people in 3 chairs problem: factorial(9) / (factorial(9 - 4))
    # so there are only 3024 permutations of "123456789" in 4 slots, 504 in 3 slots,
    # 72 in 2 slots, and 9 in 1 slot, making this brute-forceable
    assert is_pandigital(39, 186, 39*186)

    num_list = list(numbers)
    arg_lists = [list(make_ints(p.permute_all_combinations(num_list, n))) for n in range(1, 5)]
    # all pairings of arg lists, find products
    candidates = set()
    for arg_list in p.combinations(arg_lists, 2):
        for arga in arg_list[0]:
            for argb in arg_list[1]:
                candidates.add((arga, argb, arga * argb))

    pandigitals = list(filter(lambda x: is_pandigital(x[0], x[1], x[2]), candidates))

    print(f"{pandigitals} Done.")
    print(f"{sum(set([p[2] for p in pandigitals]))} Done.")


problem32()
