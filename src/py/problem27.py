# Euler discovered the remarkable quadratic formula:
#
# n2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.
#
# The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n2+an+b, where |a|<1000 and |b|≤1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

from multiprocessing import Process, Pipe, Pool

import numpy as np
import itertools as it

from util.quadratic_primes import sign_combos


def problem27():
    coefficients = np.arange(0, 1001)

    with Pool(6) as pool:
        results = pool.map_async(sign_combos, it.product(coefficients, coefficients))
        out = [r for r in results.get() if r[0] > 1]
        out.sort(reverse=True)
        print(f"Result count: {len(out)}, max: {max(out)}, out: {out}")
        print(f"Answer: {out[0][1][0] * out[0][1][1]} with prime count {out[0][0]} and coefficients {out[1]}")
    print(f"Problem 27: complete")


problem27()
