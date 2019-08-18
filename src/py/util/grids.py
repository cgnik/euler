import numpy as np


def get_sticks(grid):
    if len(grid.shape) != 2:
        return []
    rows, columns = grid.shape
    sticks = []
    for x in range(0, columns):
        for y in range(0, rows):
            if x < columns - 1:
                sticks.append((grid[y][x], grid[y][x + 1]))
            if y < rows - 1:
                sticks.append((grid[y][x], grid[y + 1][x]))
    return sticks


def routes_matching(start, routes, idx):
    return filter(lambda x: x[idx] == start, routes)


def join_path(t1, t2):
    return tuple(j for i in (t1, t2[1]) for j in (i if isinstance(i, tuple) else (i,)))


def gen_paths(data):
    grid = np.array(data)
    sticks = get_sticks(grid)
    if len(sticks) < 4:  # min possible for 2x2
        return []
    origin = grid[0][0]

    paths = list(routes_matching(origin, sticks, 0))
    while paths[0][-1] != data[-1][-1]:
        print('.',end='',flush=True)
        new_paths = []
        for path in paths:
            new_paths.extend([join_path(path, a) for a in routes_matching(path[-1], sticks, 0)])
        paths = new_paths
    return paths
