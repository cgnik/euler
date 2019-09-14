def swap(items, index1, index2):
    x = items[index1]
    items[index1] = items[index2]
    items[index2] = x


def permutations(items):
    # c is an encoding of the stack state. c[k] encodes the for-loop counter for when generate(k+1, A) is called
    c = [0 for c in range(0, len(items))]

    yield items
    # i acts similarly to the stack pointer
    i = 0
    while i < len(items):
        if c[i] < i:
            if i % 2 == 0:
                swap(items, 0, i)
            else:
                swap(items, c[i], i)
            yield items
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
