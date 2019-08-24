from statistics import mean

data = [list(map(lambda x: int(x), a.strip().split(' '))) for a in """75
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


def weight(d, row, column):
    w = [d for i in range(0, len(data) - row) for d in data[i][column:column + i]]
    if len(w) == 0:
        return data[row][column]
    return int(mean([data[row][column], mean(w)]))


def weight_data(d):
    weights = []
    for xindex, x in enumerate(d):
        weights.append([(yindex, xindex, weight(d, xindex, yindex), y) for yindex, y in enumerate(x)])
    for w in weights:
        w.sort(key=lambda x: x[2], reverse=True)
    return weights


def next_choices(c, last_index):
    return c[0] == last_index or c[0] == last_index + 1


def pathize(tiers, override={}):
    weights = weight_data(tiers)
    indices = [weights[0][0]]
    for dindex in range(1, len(tiers)):
        if override.get(dindex):
            indices.append(weights[dindex][override[dindex]])
        else:
            a, b = list(filter(lambda c: next_choices(c, indices[-1][0]), weights[dindex]))
            indices.append(a if a[2] > b[2] else b)
    return indices


def nextmax(nums, notindices):
    n = nums.copy()
    n.sort(reverse=True)
    count = 0
    idx = None
    while not idx or idx in notindices:
        idx = nums.index(n[count])
        count += 1
    return idx


def pathize_up(tiers):
    indices = []
    lastidx = None
    for i in reversed(range(0, len(tiers))):
        notindices = []
        for j in range(0, len(tiers[i])):
            maxidx = nextmax(tiers[i], notindices)
            if not lastidx or maxidx == lastidx or maxidx == lastidx - 1:
                break
        indices.append(maxidx)
        lastidx = maxidx
    indices.reverse()
    return indices


def problem18(d):
    answer_indices = pathize_up(d)
    # answer = [r[answer_indices[rindex]] for rindex, r in enumerate(d)]
    answer = [r[answer_indices[rindex]] for rindex, r in enumerate(d)]
    print(f"Answer: {sum(answer)} :: {answer}")


problem18(data)
