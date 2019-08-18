import itertools as it
from operator import mul

import numpy as np
from functools import reduce


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
