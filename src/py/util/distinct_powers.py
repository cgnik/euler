import itertools as it

import numpy as np

# NEED TO DEDUPE/SIMPLIFY_POWERS ON THE POWS LIST BEFORE USING IT. CHICKENEGG.
pows = {a ** b: (a, b) for b in range(2, 10) for a in range(2, 10)}
print(f"POWERS: {pows}")


def distinct_powers(l, h):
    values = np.arange(l, h + 1)
    terms = {simplify_powers(*p) for p in it.product(values, values)}
    print(f"terms {terms}")
    return len(terms)


def simplify_powers(base, pow):
    multiplier = pows.get(base, (1, 1))
    return int(base ** (1 / multiplier[1])), pow * multiplier[1]
