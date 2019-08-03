import threading

from util import divisible_by


class Primerator:
    def __init__(self, limit):
        self.lock = threading.Lock()
        self.limit = limit

    def find_primes(self, limit):
        primes = []
        for x in range(2, limit):
            if x % 2 == 0: continue
            divisors = filter(lambda b: (b <= int(x / 2)), primes)
            if not divisible_by(x, *divisors):
                primes.append(x)
                yield x

    def status(self, primes):
        with self.lock:
            if len(primes) % 100 == 0:
                print('.', end='')
            if len(primes) % 1000 == 0:
                print(f"latest: {primes[-1]}")

    def problem10(self):
        primes = []
        for prime in self.find_primes(self.limit):
            primes.append(prime)
            self.status(primes)
        print(f"\nAnswer: {sum(primes)}")


# 2000000
Primerator(20000).problem10()
