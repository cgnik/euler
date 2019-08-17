from unittest import TestCase

import numpy as np
from util import factors, cartesian


class Test_cartesian(TestCase):
    def test_cartesian(self):
        def lte(limit):
            def test(x):
                return x <= limit
            return test
        self.assertListEqual(listify(cartesian([1], lte(2))), [1])
        self.assertListEqual(listify(cartesian([1, 2], lte(16))), [1, 2, 4, 8, 16])
        self.assertListEqual(listify(cartesian([1, 3], lte(81))), [1, 3, 9, 27, 81])
        self.assertListEqual(listify(cartesian([1, 2, 3], lte(81))),
                             [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, 72, 81])
        self.assertListEqual(listify(cartesian([1, 2, 3], lte(1))), [1])
        self.assertListEqual(listify(cartesian([1, 2, 3], lte(2))), [1, 2])
        self.assertListEqual(listify(cartesian([1, 2, 3], lte(24))), [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24])


def listify(gen):
    x = list(np.unique(np.array([f for f in gen])))
    x.sort()
    return x
