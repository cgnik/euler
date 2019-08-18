def collatz(n):
    if n % 2 == 0:
        return int(n / 2)
    return (n * 3) + 1


def collatz_series(n):
    a = n
    while a != 1:
        a = collatz(a)
        yield a
    return 1