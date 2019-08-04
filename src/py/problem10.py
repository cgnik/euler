from primerator import Primerator
import numpy

limit = 2000000
p = Primerator(limit).primes()
with open('primes.txt', 'w') as f:
    f.write('\n'.join(map(lambda x: str(x), p)))
print(f"\nSum of primes < {limit}: {numpy.sum(p)}")
