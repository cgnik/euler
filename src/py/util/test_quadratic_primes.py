from unittest import TestCase

from util.quadratic_primes import consecutive_primes, expr, sign_combos


class Test_quadratic_primes(TestCase):
    def test_consecurive_primes(self):
        self.assertEqual(40, consecutive_primes((1, 41)))
        self.assertEqual(80, consecutive_primes((-79, 1601)))

    def test_expr(self):
        self.assertEqual(1681, expr(40, (1, 41)))

    def test_sign_combos(self):
        self.assertEqual(41, sign_combos((1, 41))[0])
