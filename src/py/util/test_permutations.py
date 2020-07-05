from unittest import TestCase

from util.permutation import permutations, permute_all, permute, combinations, permute_all_combinations


def stringify(arr):
    response = [''.join([str(a) for a in b]) for b in arr]
    response.sort()
    return response


class Test_Permutations(TestCase):
    def test_permutations(self):
        self.assertListEqual(stringify(permutations([1, 2, 3])), "123,132,213,231,312,321".split(','))
        self.assertListEqual(stringify(permutations([0, 1, 2])), "012,021,102,120,201,210".split(','))

    def test_permute(self):
        self.assertListEqual(list(permute_all(list("12"))), [["1", "2"], ["2", "1"]])
        self.assertListEqual(list(permute_all(list("123"))), [
            ['1', '2', '3'],
            ['3', '2', '1'],
            ['3', '2', '1'],
            ['1', '2', '3'],
            ['2', '1', '3'],
            ['3', '1', '2']])

    def test_combinations(self):
        self.assertListEqual(list(combinations(['1', '2'], 1)), [['1'], ['2']])
        self.assertListEqual(list(combinations(['1', '2', '3'], 1)), [['1'], ['2'], ['3']])
        self.assertListEqual(list(combinations(['1', '2', '3'], 2)), [['2', '1'], ['3', '1'], ['3', '2']])

    def test_permute_all_combinations(self):
        self.assertSetEqual(permute_all_combinations(('1', '2', '3'), 2), {
            ('1', '2'),
            ('1', '3'),
            ('2', '1'),
            ('2', '3'),
            ('3', '1'),
            ('3', '2')})
