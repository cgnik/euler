import numpy as np


def spiral_diagonals(length):
    return list(diagonal_values(2 * length - 1))


def diagonal_values(cycles):
    offset = 2
    cycle = 0
    previous = 1
    yield previous
    while cycle + 1 < cycles:
        cycle += 1
        previous += offset
        if cycle % 4 == 0:
            offset += 2
        yield previous
    return
