import numpy as np


def diagonal_values(length):
    if length % 2 == 0: raise ValueError("Cannot spiral_grid even length")
    values = [1, 3]
    offset = 0
    for l in range(2, int(length / 2) + 2):
        for r in range(0, 3 + offset):
            values.append(values[-1] + l + offset)
        offset += 1
    return values
