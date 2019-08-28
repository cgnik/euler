from statistics import mean


def weight_down(d, row, column):
    w = [d for i in range(0, len(d) - row) for d in d[i][column:column + i]]
    if len(w) == 0:
        return d[row][column]
    return int(mean([d[row][column], mean(w)]))


def weight_data_down(d):
    weights = []
    for xindex, x in enumerate(d):
        weights.append([(yindex, xindex, weight_down(d, xindex, yindex), y) for yindex, y in enumerate(x)])
    for w in weights:
        w.sort(key=lambda x: x[2], reverse=True)
    return weights


def next_choices(c, last_index):
    return c[0] == last_index or c[0] == last_index + 1


def pathize(tiers, override={}):
    weights = weight_data_down(tiers)
    indices = [weights[0][0]]
    for dindex in range(1, len(tiers)):
        if override.get(dindex):
            indices.append(weights[dindex][override[dindex]])
        else:
            a, b = list(filter(lambda c: next_choices(c, indices[-1][0]), weights[dindex]))
            indices.append(a if a[2] > b[2] else b)
    return indices


def from_index(grid, row_index, column_index):
    nexts = []
    if row_index > len(grid):
        return nexts
    row = grid[row_index + 1]
    if column_index < len(row):
        nexts.append(row[column_index])
    if column_index > 0:
        nexts.append(row[column_index - 1])
    return nexts


def weight_up(grid, row_index, column_index):
    weights = [grid[row_index][column_index]]
    next_weights = from_index(grid, row_index, column_index)
    if len(next_weights):
        weights.append(mean(next_weights))
    return sum(weights)


def next_index(grid, row_index, column_index):
    ln = len(grid[row_index])
    if column_index == 0 or ln == 1:
        return 0
    elif column_index >= ln:
        return ln - 1
    elif weight_up(grid, row_index, column_index) < weight_up(grid, row_index, column_index - 1):
        return column_index - 1
    return column_index


def pathize_up(triangle):
    tiers = triangle.copy()
    tiers.reverse()
    max_path = [0]
    paths = []
    for num_index, num in enumerate(tiers[0]):
        path = [(num_index, num)]
        for tier_index, tier in enumerate(tiers):
            if tier_index == 0: continue
            up_index = next_index(tiers, tier_index, path[-1][0])
            path.append((up_index, tier[up_index]))
        # print(f"path: {path}")
        addends = [x[1] for x in path]
        if sum(addends) > sum(max_path):
            max_path = addends
    max_path.reverse()
    return max_path


def problem18up(d):
    answer = pathize_up(d)
    print(f"Up-path answer: {sum(answer)} :: {answer}")


def elaborate(d, row, column):
    if row < len(d) - 1:
        paths = elaborate(d, row + 1, column) + elaborate(d, row + 1, column + 1)
        for p in paths:
            p.insert(0, d[row][column])
        return paths
    return [[d[row][column]]]


def problem18brute(d):
    all = [(sum(e), e) for e in elaborate(d, 0, 0)]
    best = max(all, key=lambda x: x[0])
    # answer: (1074, [75, 64, 82, 87, 82, 75, 73, 28, 83, 32, 91, 78, 58, 73, 93])
    print(f"Brute answer: {best}")


def problem18():
    d = [list(map(lambda x: int(x), a.strip().split(' '))) for a in """75
                              95 64
                            17 47 82
                          18 35 87 10
                        20 04 82 47 65
                      19 01 23 75 03 34
                    88 02 77 73 07 63 67
                  99 65 04 28 06 16 70 92
                41 41 26 56 83 40 80 70 33
              41 48 72 33 47 32 37 16 94 29
            53 71 44 65 25 43 91 52 97 51 14
          70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
      63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split("\n")]
    problem18brute(d)
    problem18up(d)


problem18()
