from util.factoring import is_prime_quick
import numpy as np


def expr(n, ab):
    return n ** 2 + (ab[0] * n) + ab[1]


def consecutive_primes(ab):
    n = 0
    while True:
        n += 1
        if not is_prime_quick(expr(n, ab)):
            return n
    return 0


signs = np.array([(-1, 1), (1, -1), (-1, -1), (1, 1)])


def sign_combos(coeff):
    return max([(consecutive_primes(ab), tuple(ab)) for ab in (signs * coeff)])
