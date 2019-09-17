import numpy as np

import itertools as it
import numpy as np


def distinct_powers(l, h):
    v = np.arange(l, h + 1)
    return {pow(t[0], t[1]) for t in it.product(v, v)}
