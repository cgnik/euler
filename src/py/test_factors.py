from unittest import TestCase

import numpy as np
from util import factors


class Test_factors(TestCase):
    def test_any_divisors(self):
        self.assertListEqual(listify(factors(1)), [1])
        self.assertListEqual(listify(factors(12)), [1, 2, 3, 12])
        self.assertListEqual(listify(factors(8)), [1, 2, 8])
        self.assertListEqual(listify(factors(9)), [1, 3, 9])
        self.assertListEqual(listify(factors(5)), [1, 5])
        self.assertListEqual(listify(factors(22)), [1, 2, 11, 22])
        self.assertListEqual(listify(factors(25)), [1, 5, 25])
        self.assertListEqual(listify(factors(63)), [1, 3, 7, 63])


def listify(gen):
    x = list(np.unique(np.array([f for f in gen])))
    x.sort()
    return x

