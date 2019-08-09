from math import sqrt
import numpy as np


def is_divisible(a, b):
    return a % b == 0


def any_divisors(a, bs):
    if not bs: return False
    for b in iter(bs):
        yield is_divisible(a, b)
    return False


def divisible_by(a, bs):
    return any(any_divisors(a, bs))


def factors(num):
    factor = int(sqrt(num))
    print(f"starting factorization with {factor}")
    while factor % 2 == 0:
        factor = int(factor / 2)
    while num > 1:
        if num % factor == 0:
            yield factor
            num = int(num / factor)
        factor -= 2
    yield num


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
    for i in range(0, dim):
        hd = x.diagonal(offset=(-1 * i))
        a[i][0:len(hd)] = hd
    return a
