def permutations(items):
    # c is an encoding of the stack state. c[k] encodes the for-loop counter for when generate(k+1, A) is called
    c = [0 for c in range(0, len(items))]

    yield items
    # i acts similarly to the stack pointer
    i = 0
    while i < len(items):
        if c[i] < i:
            if i % 2 == 0:
                items[0], items[i] = items[i], items[0]
            else:
                items[c[i]], items[i] = items[i], items[c[i]]
            yield items
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1


def gen_bits(bit_count, max_bits):
    end = pow(2, max_bits)
    for i in range(0, end):
        if bin(i).count('1') == bit_count:
            yield i


def combinations(people, seat_count=0):
    people_count = len(people)
    if seat_count < 1:
        seat_count = len(people)
    # assumption: len(people) >= seats
    # strategy: use a bit to rep a single person
    # generate all possible numbers with bit array of len(people)
    # find all values in that list with seat_count bits turned on
    # map back onto people and output
    bits_format = "{0:>0" + str(people_count) + "b}"
    results = []
    for combo in gen_bits(seat_count, len(people)):
        result = []
        for i in range(people_count - 1, -1, -1):
            if (1 << i) & combo:
                result.append(people[i])
        results.append(result)
    return results


def permute(a, k):
    # heap's algorithm
    if k == 1:
        yield a.copy()
    else:
        yield from permute(a, k - 1)
        for i in range(0, k - 1):
            target = 0
            if k % 2 == 0:
                target = i - 1
            a[target], a[i] = a[i], a[target]
            yield from permute(a, k - 1)


def permute_all(a):
    return permute(a, len(a))


def permute_all_combinations(a, length):
    results = []
    for c in combinations(a, length):
        results += permute_all(c)
    return set(map(tuple, results))
