from unittest import TestCase

from util import divisible_by


class Test_divisible_by(TestCase):
    def test_any_divisors(self):
        self.assertTrue(divisible_by(12, 5, 6, 2))
        self.assertTrue(divisible_by(8, 2))
        self.assertTrue(divisible_by(9, 3))
        self.assertFalse(divisible_by(5, 2, 3))
        self.assertFalse(divisible_by(22, 10, 45, 7))
        self.assertTrue(divisible_by(22, 10, 45, 11))
        self.assertTrue(divisible_by(63, 88, 2, 3))
        self.assertFalse(divisible_by(63, 88, 2, 5))
