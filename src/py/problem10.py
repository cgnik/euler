import threading

from util import divisible_by, is_prime_quick


def candidates():
    x = 3
    while True:
        x += 2
        yield x
    yield


class PrimeCandidateGenerator:
    def __init__(self):
        self.lock = threading.Lock()
        self.it = candidates()

    def __iter__(self):
        return self

    def __next__(self):
        with self.lock:
            return self.it.__next__()


class Primerator:
    def __init__(self, limit):
        self.limit = limit
        self.accumulator = [2]
        self.generator = PrimeCandidateGenerator()
        self.prime_lock = threading.Lock()

    def _status_(self, primes):
        if not len(primes): return
        if len(primes) % 100 == 0:
            print('.', end='', flush=True)
        if len(primes) % 1000 == 0:
            print(f"latest: {primes[-1]}; {len(primes)} found so far.")

    def _add_prime_(self, x):
        with self.prime_lock:
            self.accumulator.append(x)
            self._status_(self.accumulator)

    def _one_thread_(self):
        for candidate in self.generator:
            if candidate > self.limit:
                break
            if is_prime_quick(candidate):
                self._add_prime_(candidate)

    def primes(self, thread_count=8):
        threads = []
        for i in range(0, thread_count):
            threads.append(threading.Thread(target=self._one_thread_))
            threads[-1].start()
            for t in threads: t.join()
        return self.accumulator


# 2000000
p = Primerator(2000000).primes()
print(f"PRIMES: {p}\n\nAnswer: {sum(p)}")
