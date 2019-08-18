def is_divisible(a, b):
    return a % b == 0


def any_divisors(a, bs):
    if not bs: return False
    for b in iter(bs):
        yield is_divisible(a, b)
    return False


def divisible_by(a, bs):
    return any(any_divisors(a, bs))