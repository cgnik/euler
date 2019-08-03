import threading

from util import divisible_by


class Primerator:
    def __init__(self, limit, thread_count):
        self.thread_count = thread_count
        self.limit = limit
        self.accumulator = []
        self.output_lock = threading.Lock()
        self.yield_lock = threading.Lock()
        self.prime_lock = threading.Lock()

    def _find_primes_(self, limit):
        primes = []
        for x in range(2, limit):
            if x % 2 == 0: continue
            divisors = filter(lambda b: (b <= int(x / 2)), primes)
            if not divisible_by(x, *divisors):
                primes.append(x)
                with self.yield_lock:
                    yield x
        yield None

    def _status_(self, primes):
        with self.output_lock:
            if len(primes) % 100 == 0:
                print('.', end='')
            if len(primes) % 1000 == 0:
                print(f"latest: {primes[-1]}")

    def _one_thread_(self):
        last_prime = 0
        for prime in self._find_primes_(self.limit):
            if not prime:
                break
            with self.prime_lock:
                last_prime = prime
                self.accumulator.append(prime)
            self._status_(self.accumulator)
        print(f"Thread exiting; {last_prime}")

    def primes(self):
        threads = []
        for i in range(0, self.thread_count):
            threads.append(threading.Thread(target=self._one_thread_))
            threads[-1].start()
        for t in threads:
            t.join()
        return self.accumulator


# 2000000
p = Primerator(20000, 8).primes()
print(f"\nAnswer: {sum(p)}")
