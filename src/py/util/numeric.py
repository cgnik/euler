def ticklog(count, increment):
    if count % increment == 0:
        print(".", end='', flush=True)


def naturals(seed=1):
    num = seed
    while True:
        yield num
        num += 1


def triangles():
    last = 0
    for n in naturals():
        last = n + last
        yield last
