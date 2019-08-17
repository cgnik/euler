from unittest import TestCase

import numpy as np
from util import factors, cartesian


class Test_cartesian(TestCase):
    def test_cartesian(self):
        self.assertListEqual(listify(cartesian([1])), [1])
        self.assertListEqual(listify(cartesian([1, 2])), [1, 2, 4, 8, 16])
        self.assertListEqual(listify(cartesian([1, 3])), [1, 3, 9, 27, 81])
        self.assertListEqual(listify(cartesian([1, 2, 3])), [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 36, 54, 81])


def listify(gen):
    x = list(np.unique(np.array([f for f in gen])))
    x.sort()
    return x
