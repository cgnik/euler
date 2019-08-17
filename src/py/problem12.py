import numpy as np
import itertools as it
from util import factors, ticklog


def cartesian(x):
    cart = np.array([p for p in it.product(x, x, x, x)])
    return cart.prod(axis=1)


def cartesian_factors(n, facs):
    # THIS IS INADEQUATE - SKIPS THINGS LIKE 2**5 WHEN 2 APPEARS QUINCE IN FACTORS
    cart = np.unique(list(cartesian(facs)))
    return facs, cart[np.where(n % cart == 0)]


def naturals(seed=1):
    num = seed
    while True:
        yield num
        num += 1


def triangles():
    last = 0
    for n in naturals():
        last = n + last
        yield last


def triangulate(start=2 ** 30, limit=100):
    count = 0
    for x in triangles():
        count += 1
        if x > start:
            facs = list(factors(x, log=False))
            if len(facs) > limit:
                return x, facs
            else:
                yield x, facs


def problem12():
    # 16792205430
    start_threshold = 16792205430
    for answer in triangulate(start_threshold):
        cart = cartesian_factors(answer[0], answer[1])
        # print(f"\nN:{answer[0]}:\n\tfactors: {answer[1]};\n\tcartesian {cart}")
        # print(f"N:{answer[0]}: carts: {cart}")
        if len(cart[1]) > 300: print(f"N:{answer[0]}: cartlen: {len(cart[1])}")


problem12()

# try 3: what is the smallest set of primes whose cartesian product is 500 numbers, and thus to the target
#
# def cartesian(x, y):
#     cart = np.array([p for p in it.product(x, y)])
#     print(f"cart length: {len(cart)}")
#     prods = np.unique(np.array([a * b for a, b in cart]))
#     return prods
#
#
# def all_factors(n):
#     facs = np.unique(list(factors(n)))
#     cart = np.unique(list(cartesian(facs, facs)))
#     return (facs, cart[np.where(n % cart == 0)])
#
#
# def problem12(seed):
#     f = all_factors(seed)
#     print(f"seed {seed}: \n\tfactors ({len(f[0])}) {f[0]} : \n\tcartesia ({len(f[1])})n {f[1]}")
#
#
# seed = np.product(np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]))
# problem12(seed)

#
#
# def cartesian(x, y):
#     cart = np.array([p for p in it.product(x, y)])
#     prods = np.unique(np.array([a * b for a, b in cart]))
#     return prods
#
#
#
# def all_factors(n):
#     max_fac = int(n / 2)
#     facs = np.array([f for f in factors(n)])
#     while facs.max() < max_fac:
#         print(",", end='', flush=True)
#         facs = cartesian(facs, facs)
#     facs = facs[np.less(facs, max_fac)]
#     return facs[np.where(n % facs == 0)]
#
#
# def problem12(seed):
#     facs = np.array((0, 0))
#     n = seed
#     while facs.size < 500:
#         n *= 10
#         facs = all_factors(n)
#         print(f"Factors: {facs}.", flush=True)
#     print(f"factors ({facs}): {facs}")
#
#
# # seed = 100000000000000000
# seed = 100000000000000000000 / 2
# problem12(seed)
