# https://projecteuler.net/problem=32
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
import sys


def is_pandigital(x, c):
    p = x * c
    s = list('{}{}{}'.format(x, c, p))
    s.sort()
    return ''.join(s) == "123456789"


def gen_bits(bit_count, max_bits):
    end = pow(2, max_bits) + 1
    for i in range(0, end):
        if bin(i).count('1') == bit_count:
            yield i


def combinations(people, seat_count=0):
    if seat_count < 1:
        seat_count = len(people)
    # assumption: len(people) >= seats
    # strategy: use a bit to rep a single person
    # generate all possible numbers with bit array of len(people)
    # find all values in that list with seat_count bits turned on
    # map back onto people and output
    results = []
    for combo in gen_bits(seat_count, len(people)):
        print(f"result: {combo:>08b}")


def permute(a, k):
    # heap's algorithm
    if k == 1:
        yield a.copy()
    else:
        yield from permute(a, k - 1)
        for i in range(0, k - 1):
            if k % 2 == 0:
                a[i], a[i - 1] = a[i - 1], a[i]
            else:
                a[0], a[i] = a[i], a[0]
            yield from permute(a, k - 1)


def permute_all(a):
    return permute(a, len(a))


def problem32():
    # strategy: brute force: permutations of "123456789"
    # broken into 3 strings
    # strings for the multiplicands must be 1-4 characters, each, no more,
    # considering that the use of 5 characters on the left of = would
    # necessitate the presence of no more than 4 on the right, which could
    # only be true if it was something like 2*4-digit=other-4-digit
    # this is like a 5 peopl in 3 chairs problem: factorial(9) / (factorial(9 - 4))
    # so there are only 3024 permutations of "123456789" in 4 slots, 504 in 3 slots,
    # 72 in 2 slots, and 9 in 1 slot, making this brute-forceable
    assert is_pandigital(39, 186)
    assert list(permute_all(list("12"))) == [["1", "2"], ["2", "1"]]
    assert list(permute_all(list("123"))) == [
        ['1', '2', '3'],
        ['3', '2', '1'],
        ['3', '2', '1'],
        ['1', '2', '3'],
        ['2', '1', '3'],
        ['3', '1', '2']]
    print(f"Done.")


problem32()
