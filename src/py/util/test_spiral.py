from unittest import TestCase

from util.spiral import diagonal_values


class Test_spiral(TestCase):
    def test_spiral_grid(self):
        self.assertRaises(ValueError, lambda: diagonal_values(4))
        self.assertEqual(25, sum(diagonal_values(3)))
        self.assertEqual(101, sum(diagonal_values(5)))
