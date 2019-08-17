from math import sqrt, ceil
import itertools as it
import numpy as np


def ticklog(count, increment):
    if count % increment == 0:
        print(".", end='', flush=True)


def is_divisible(a, b):
    return a % b == 0


def any_divisors(a, bs):
    if not bs: return False
    for b in iter(bs):
        yield is_divisible(a, b)
    return False


def divisible_by(a, bs):
    return any(any_divisors(a, bs))


def factors(num, log=True, primes_only=False):
    if log: print(f"factoring {num}: ", end='', flush=True)
    target = num
    max_factor = int(sqrt(num))
    yield 1
    for x in [2, 3, 5]:
        while target % x == 0:
            yield x
            target = int(target / x)
    factor = 5
    factor_count = 0
    while factor <= max_factor:
        factor += 1
        while target % factor == 0:
            if log: print(".", end='', flush=True)
            factor_count += 1
            yield factor
            target = int(target / factor)
    # fall-through large factor case, like 22/11
    if num % target == 0: yield target
    if not primes_only: yield num
    if log: print("Done.", flush=True)


def all_factors(num):
    factor = num
    while factor > 0:
        if num % factor == 0:
            yield factor
        if factor > num / 2:
            factor = int(factor / 2)
            yield 2
        else:
            factor -= 1


def is_palindrome(x):
    s = str(x)
    end = len(s) - 1
    for i in range(0, len(s)):
        if s[i] != s[end - i]:
            return False
    return True


def find_palindromes():
    all = []
    for i in range(100, 999):
        for j in range(100, 999):
            if is_palindrome(i * j):
                all.append((i * j, i, j))
    return all


def is_prime(x, lower_primes):
    divisors = filter(lambda b: (b <= int(x / 2)), lower_primes)
    return not divisible_by(x, divisors)


def is_prime_quick(x):
    if x <= 3:
        return x > 1
    elif x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        # while i * 3 <= x: // works exactly the same as above, though more cycles
        if x % i == 0: return False
        i += 2
    return True


def groups(x, size, start=0):
    return np.vstack([x[:, n:n + size] for n in range(start, x.shape[0] - size + 1) if len(x[n]) >= size])


def flipdiag(x, dim):
    a = np.zeros((dim, dim))
    for i in range(-1 * dim, dim):
        hd = x.diagonal(offset=i)
        a[i][0:len(hd)] = hd
    return a


def cartesian(x):
    cart = np.array([p for p in it.product(x, x, x, x)])
    return cart.prod(axis=1)


def cartesian_factors(n, facs):
    # THIS IS INADEQUATE - SKIPS THINGS LIKE 2**5 WHEN 2 APPEARS QUINCE IN FACTORS
    cart = np.unique(list(cartesian(facs)))
    return facs, cart[np.where(n % cart == 0)]


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
