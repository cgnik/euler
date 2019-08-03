from math import sqrt


def is_divisible(a, b):
    return a % b == 0


def any_divisors(a, *bs):
    for b in bs:
        yield is_divisible(a, b)


def divisible_by(a, *bs):
    return len(bs) > 0 and any(any_divisors(a, *bs))


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
