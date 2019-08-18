from unittest import TestCase

import numpy as np
from collatz import collatz, collatz_series
from cartesian import cartesian
from factoring import factors


class Test_collatz(TestCase):
    def test_collatz(self):
        self.assertEqual(collatz(13), 40)
        self.assertEqual(collatz(40), 20)

    def test_collatz_series(self):
        self.assertListEqual(list(collatz_series(13)), [40, 20, 10, 5, 16, 8, 4, 2, 1])
