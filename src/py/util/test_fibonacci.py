from unittest import TestCase

from util.fibonacci import fibonacci


class Test_fibonacci(TestCase):
    def test_fibonacci(self):
        def nth_fibonacci(n):
            count = 0
            for f in fibonacci():
                count += 1
                if count >= n:
                    break;
            return f

        self.assertEqual(21, nth_fibonacci(8))
        self.assertEqual(144, nth_fibonacci(12))
