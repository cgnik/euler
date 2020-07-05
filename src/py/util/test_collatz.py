from unittest import TestCase

from util.collatz import collatz, collatz_series


class Test_collatz(TestCase):
    def test_collatz(self):
        self.assertEqual(collatz(13), 40)
        self.assertEqual(collatz(40), 20)

    def test_collatz_series(self):
        self.assertListEqual(list(collatz_series(13)), [40, 20, 10, 5, 16, 8, 4, 2, 1])
