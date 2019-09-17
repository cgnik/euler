from unittest import TestCase

from util.distinct_powers import distinct_powers


class Test_distinct_powers(TestCase):
    def test_distinct_powers(self):
        self.assertSetEqual(distinct_powers(2, 5), {4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125})
