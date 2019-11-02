from unittest import TestCase

from util.distinct_powers import distinct_powers, simplify_powers


class Test_distinct_powers(TestCase):
    def test_distinct_powers(self):
        # self.assertSetEqual(distinct_powers(2, 5), {4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125})
        self.assertEqual(distinct_powers(2, 5), 15)

    def test_simplify_powers(self):
        self.assertEqual(simplify_powers(4, 2), (2, 4))
        self.assertEqual(simplify_powers(9, 2), (3, 4))
        self.assertEqual(simplify_powers(16, 2), (2, 8))
        self.assertEqual(simplify_powers(2, 2), (2, 2))
