from unittest import TestCase

from util.spiral import spiral_diagonals


class Test_spiral(TestCase):
    def test_spiral_diagonals(self):
        self.assertListEqual(spiral_diagonals(3), [1, 3, 5, 7, 9])
        self.assertListEqual(spiral_diagonals(5), [1, 3, 5, 7, 9, 13, 17, 21, 25])
        self.assertListEqual(spiral_diagonals(11),
                             [1, 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49, 57, 65, 73, 81, 91, 101, 111, 121])
