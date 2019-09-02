from unittest import TestCase

import numpy as np
from util.factoring import factors, all_factors


class Test_factors(TestCase):
    def test_factors(self):
        self.assertListEqual(listify(factors(1)), [1])
        self.assertListEqual(listify(factors(12)), [1, 2, 3, 12])
        self.assertListEqual(listify(factors(8)), [1, 2, 8])
        self.assertListEqual(listify(factors(9)), [1, 3, 9])
        self.assertListEqual(listify(factors(5)), [1, 5])
        self.assertListEqual(listify(factors(22)), [1, 2, 11, 22])
        self.assertListEqual(listify(factors(25)), [1, 5, 25])
        self.assertListEqual(listify(factors(63)), [1, 3, 7, 63])
        self.assertListEqual(listify(factors(1210)), [1, 2, 5, 11, 1210])

    def test_all_factors(self):
        self.assertListEqual(listify(all_factors(220)), [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])
        self.assertListEqual(listify(all_factors(284)), [1, 2, 4, 71, 142])
        self.assertListEqual(listify(all_factors(1210)), [1, 2, 5, 10, 11, 22, 55, 110, 121, 242, 605])


def listify(gen):
    x = list(np.unique(np.array([f for f in gen])))
    x.sort()
    return x
