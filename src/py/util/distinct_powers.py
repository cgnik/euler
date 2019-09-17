import itertools as it

import numpy as np


def distinct_powers(l, h):
    values = np.arange(l, h + 1)
    terms = {exp_by_squaring(t[0], t[1]) for t in it.product(values, values)}
    print(f"terms: {terms}")
    # terms = np.asarray([t for t in it.product(values, values)], dtype=np.uint64)
    # powers = {u for u in np.power(terms[:, 0], terms[:, 1], dtype=np.uint64)}
    # print(f"powers {powers}")
    return terms


def exp_by_squaring(x, n):
    return _exp_by_squaring_(1, x, n)


def _exp_by_squaring_(y, x, n):
    if n < 0:
        return _exp_by_squaring_(y, 1 / x, - n)
    elif n == 0:
        return y
    elif n == 1:
        return x * y
    elif n % 2 == 0:
        return _exp_by_squaring_(y, x * x, n / 2)
    elif n % 2 == 1:
        return _exp_by_squaring_(x * y, x * x, (n - 1) / 2)
