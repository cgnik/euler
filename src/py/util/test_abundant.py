from unittest import TestCase

from util.abundant import abundant_numbers, contains_sum_for


class Test_abundants(TestCase):
    test_data1 = []
    test_data2 = [[1, 2], [3, 4]]
    test_data3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def test_abundants(self):
        self.assertListEqual(abundant_numbers(120),
                             [12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96, 100,
                              102, 104, 108, 112, 114, 120])

    def test_contains_sum_for(self):
        self.assertTrue(contains_sum_for(3, [1, 2]))
        self.assertFalse(contains_sum_for(3, [2, 2]))
        self.assertTrue(contains_sum_for(15, [1, 2, 3, 4, 5, 10, 20, 30, 40]))
        self.assertFalse(contains_sum_for(15, [1, 2, 3, 4, 5, 20, 30, 40]))
