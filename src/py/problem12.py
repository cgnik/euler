from util import cartesian_factors, factors, triangles


def triangulate(start=2 ** 30, limit=100):
    count = 0
    for x in triangles():
        count += 1
        if x > start:
            facs = list(factors(x, log=False))
            if len(facs) > limit:
                return x, facs
            else:
                yield x, facs


def problem12():
    # N: 725145761340: cartlen: 490
    start_threshold = 925517539128  # is the best so far
    print(f"Starting factorization of triangles with {start_threshold}")
    count = 0
    for answer in triangulate(start_threshold):
        cart = cartesian_factors(answer[0], answer[1])
        # print(f"N:{answer[0]}: carts: {cart}")
        if len(cart[1]) > 300: print(f"N:{answer[0]}: cartlen: {len(cart[1])}")
        if count > 5: break


problem12()
