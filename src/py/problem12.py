from util.numeric import triangles
from util.cartesian import cartesian_factors
from util.factoring import factors


def triangulate(start=2 ** 30, limit=100):
    count = 0
    for x in triangles():
        count += 1
        if x >= start:
            facs = list(factors(x, log=False))
            facs.remove(x)
            if len(facs) > limit:
                return x, facs
            else:
                yield x, facs

def verify(n, facs):
    for f in facs:
        if n % f != 0:
            raise ValueError(f"{n} is NOT evenly divisible by {f}")

def problem12():
    # N: 725145761340: cartlen: 490
    # start_threshold = 925517539128  # is the best so far
    # start_threshold = 725145761340  # is the best so far
    start_threshold = 55
    print(f"Starting factorization of triangles with {start_threshold}")
    best_len = 0
    for answer in triangulate(start_threshold):
        cart = cartesian_factors(answer[0], answer[1])
        print(f"N: {answer[0]} ({len(cart[1])})")
        if len(cart[1]) > 500: break
    verify(answer[0], cart[1])
    print(f"Answer: {answer[0]}\nFactor Count: {len(cart[1])}\n\tFactors: {cart}")

problem12()
# answer appears to be : 76576500