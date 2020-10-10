# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?
# https://projecteuler.net/problem=35

from util.primerator import is_prime_quick as is_prime


def digits(num):
    if num == 0:
        yield 0
    n = num
    while n > 0:
        yield n % 10
        n = int(n / 10)


def is_circular_prime(x):
    s = list(str(x))
    for r in range(0, len(str(x))):
        g = s[r:] + s[0:r]
        if not is_prime(int(''.join([str(pp) for pp in g]))):
            return False
    return True


def circular_primes(limit):
    if limit > 2:
        yield 2
    for x in range(1, limit, 2):
        print(f"\rTesting {x:07d}", end='', flush=True)
        if is_circular_prime(x):
            print(f"\r \u2713 {x:07d}", flush=True)
            yield x
    print('\nDone.')


def init_test():
    expected = {2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199}
    actual = set(list(circular_primes(200)))
    assert expected.intersection(
        actual) == expected, f"Test failed to generate expected results: \nexpect: {expected}\nactual: {actual}"


def problem35():
    init_test()
    cyclics = list(circular_primes(10 ** 6))
    print(f"answer: {len(cyclics)}, cyclics: {cyclics}")


problem35()
