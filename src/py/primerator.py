from multiprocessing import Pool

from util import is_prime_quick


class Primerator:

    def __init__(self, limit):
        self.limit = limit

    def _candidate_generator_(self):
        for x in range(3, self.limit, 2):
            yield x

    def _one_thread_(self, candidate):
        if candidate % 100000 == 1: print('.', end='', flush=True)
        return candidate, is_prime_quick(candidate)

    def _filter_primes_(self, candidates):
        return filter(lambda x: x[1], candidates)

    def primes(self, thread_count=8):
        p = Pool(thread_count)
        results = p.map(self._one_thread_, self._candidate_generator_())
        answers = [2]
        answers.extend(map(lambda y: y[0], self._filter_primes_(results)))
        return answers
