from unittest import TestCase

from util.fibonacci import fibonacci


class Test_fibonacci(TestCase):
    def test_fibonacci(self):
        self.assertEqual(3, next(fibonacci()))
