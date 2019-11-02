import itertools as it
from operator import mul

import numpy as np
from functools import reduce

from util.factoring import factors


def cartesian(boundary, x, *args, reducer=mul):
    products = x
    last_products = []

    def gen():
        yield x
        if args and len(args):
            for z in args:
                yield z
        else:
            while True: yield products
        return None

    for products in gen():
        products = np.unique([reduce(reducer, x) for x in it.product(x, products)])
        products = list(filter(boundary, products))
        products.sort()
        if products == last_products:
            break
        last_products = products
    return np.array(products)


def cartesian_factors(n, facs):
    cart = cartesian(lambda x: n % x == 0, facs)
    return facs, cart[np.where(n % cart == 0)]


def cartesian_product(nums, limit=None):
    product_pairs = it.product(np.array(nums), np.array(nums))
    products = [a[0] * a[1] for a in product_pairs]
    if limit is not None:
        divisors = list(filter(lambda x: limit % x == 0, products))
    else:
        divisors = products
    return divisors


def cartesian_loop(n, count):
    facs = list(factors(n))
    for c in range(0, count):
        facs = list(set(cartesian_product(facs, n)))
    return facs


def all_factors(num, include_self=False):
    answer = cartesian_loop(num, 8)
    if not include_self:
        answer.remove(num)
    return answer
