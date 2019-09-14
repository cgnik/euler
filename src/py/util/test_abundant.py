from unittest import TestCase

from util.abundant import abundant_numbers, contains_sum_for


class Test_abundants(TestCase):
    test_data1 = []
    test_data2 = [[1, 2], [3, 4]]
    test_data3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def test_abundants_wierdos(self):
        # [1, 2, 4, 11, 22, 44, 121, 242, 253, 484, 506, 1012, 2783, 5566]
        # [1, 2, 4, 11, 22, 23, 44, 46, 92, 121, 242, 253, 484, 506, 1012, 2783, 5566]
        abundants = abundant_numbers(11493)
        self.assertTrue(11132 in abundants)
        self.assertTrue(11492 in abundants)
    #
    # def test_abundants(self):
    #     self.assertListEqual(abundant_numbers(270), [12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78,
    #                                                  80, 84, 88, 90, 96, 100, 102, 104, 108, 112, 114, 120, 126,
    #                                                  132, 138, 140, 144, 150, 156, 160, 162, 168, 174, 176, 180,
    #                                                  186, 192, 196, 198, 200, 204, 208, 210, 216, 220, 222, 224,
    #                                                  228, 234, 240, 246, 252, 258, 260, 264, 270])
    #
    # def test_contains_sum_for(self):
    #     self.assertTrue(contains_sum_for(3, [1, 2]))
    #     self.assertFalse(contains_sum_for(3, [2, 2]))
    #     self.assertTrue(contains_sum_for(15, [1, 2, 3, 4, 5, 10, 20, 30, 40]))
    #     self.assertTrue(contains_sum_for(15, [1, 2, 3, 4, 5, 13, 20, 30, 40]))
    #     self.assertFalse(contains_sum_for(15, [1, 2, 3, 4, 5, 20, 30, 40]))
    #     self.assertTrue(contains_sum_for(24, [12, 17, 20]))
    #     self.assertTrue(contains_sum_for(7141, [1, 444, 7723, 7140, 8002]))
    #     self.assertTrue(contains_sum_for(34, [12, 17, 20]))
    #     self.assertFalse(contains_sum_for(19, [12, 13, 14, 15, 17, 20]))
    #     self.assertFalse(contains_sum_for(11132, []))
    #     self.assertFalse(contains_sum_for(11492, []))
