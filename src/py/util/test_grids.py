from unittest import TestCase

import numpy as np

from util.grids import gen_paths, get_sticks


class Test_grids(TestCase):
    test_data1 = []
    test_data2 = [[1, 2], [3, 4]]
    test_data3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def test_get_sticks(self):
        self.assertCountEqual(get_sticks(np.array(self.test_data1)), [])
        self.assertCountEqual(get_sticks(np.array(self.test_data2)), [(1, 2), (1, 3), (2, 4), (3, 4)])
        self.assertCountEqual(get_sticks(np.array(self.test_data3)), [(1, 2), (1, 4), (2, 5), (2, 3), (3, 6),
                                                                      (4, 5), (4, 7), (5, 6), (5, 8), (6, 9), (7, 8),
                                                                      (8, 9)])

    def test_20_sticks(self):
        # it's always 2(n^2) - 2n
        def sickerize(n):
            arr = np.arange(n ** 2).reshape((n, n))
            x = get_sticks(arr)
            print(f"{n} sticks: {len(x)}\n\tX :: {x}")

        for n in [2, 3, 6, 7, 8, 9, 20]:
            sickerize(n)

    def test_gen_paths_sanity(self):
        self.assertListEqual(gen_paths(None), [])
        self.assertListEqual(gen_paths(self.test_data1), [])

    def test_gen_paths_basic(self):
        self.assertListEqual(gen_paths(self.test_data2), [(1, 2, 4), (1, 3, 4)])

    def test_gen_paths_complex(self):
        self.assertListEqual(gen_paths(self.test_data3), [
            (1, 2, 3, 6, 9),
            (1, 2, 5, 6, 9),
            (1, 2, 5, 8, 9),
            (1, 4, 5, 6, 9),
            (1, 4, 5, 8, 9),
            (1, 4, 7, 8, 9),
        ])
