from math import sqrt

from util.divisible import divisible_by


def factors(num):
    n = num
    yield 1
    for x in [2, 3, 5, 7]:
        while n % x == 0:
            n = int(n / x)
            yield x
    f = 11
    while f <= int(sqrt(n)):
        if n % f == 0:
            yield f
            while n % f == 0:
                n = int(n / f)
        f += 2
    # compensate for 22/11 problem
    if num % n == 0: yield n
    yield num


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
