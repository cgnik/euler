from unittest import TestCase

from util.digit_exponents import is_power_sum, power_sums


class TestDigitExponents(TestCase):
    def test_is_power_sum(self):
        self.assertTrue(is_power_sum(1634, 4))
        self.assertTrue(is_power_sum(8208, 4))
        self.assertTrue(is_power_sum(9474, 4))
        self.assertFalse(is_power_sum(5, 4))
        self.assertFalse(is_power_sum(8238, 4))
        self.assertFalse(is_power_sum(9187324182347, 4))

    def test_power_sums(self):
        self.assertListEqual(list(power_sums(4, 2000)), [1634])
        self.assertListEqual(list(power_sums(4, 9000)), [1634, 8208])
        self.assertListEqual(list(power_sums(4, 9500)), [1634, 8208, 9474])
