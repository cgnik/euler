from util import divisible_by


def find_primes(limit):
    primes = []
    for x in range(2, limit):
        if x % 2 == 0: continue
        divisors = filter(lambda b: (b <= int(x / 2)), primes)
        if not divisible_by(x, *divisors):
            primes.append(x)
            yield x


def status(primes):
    if len(primes) % 100 == 0:
        print('.', end='')
    if len(primes) % 1000 == 0:
        print(f"latest: {primes[-1]}")


def problem10():
    limit = 2000000
    primes = []
    for prime in find_primes(limit):
        primes.append(prime)
        status(primes)
    print(f"\nPrimes: {primes}\nAnswer: {sum(primes)}")


problem10()
