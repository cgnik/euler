import numpy as np

from util.grids import gen_paths


def problem15():
    big_grid = np.arange(20 ** 2).reshape((20, 20))
    print(gen_paths(big_grid))


problem15()
