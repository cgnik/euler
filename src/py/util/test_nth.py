from unittest import TestCase

from util.nth import nth


class Test_nth(TestCase):
    def test_nth(self):
        self.assertEqual(1, nth(3, [0, 2, 1]))
        self.assertEqual(0, nth(-33, [0, 2, 1]))

        def test_gen(max):
            for i in range(0, max):
                yield i

        self.assertEqual(2, nth(3, test_gen(4)))
        self.assertEqual(2, nth(3, test_gen(8)))
