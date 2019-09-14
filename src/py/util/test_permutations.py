from unittest import TestCase

from util.permutation import permutations


def stringify(arr):
    response = [''.join([str(a) for a in b]) for b in arr]
    response.sort()
    return response


class Test_Permutations(TestCase):
    def test_permutations(self):
        self.assertListEqual(stringify(permutations([1, 2, 3])), "123,132,213,231,312,321".split(','))
        self.assertListEqual(stringify(permutations([0, 1, 2])), "012,021,102,120,201,210".split(','))
