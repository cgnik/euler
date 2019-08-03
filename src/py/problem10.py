import time

from util import divisible_by


def problem10():
    primes = [2]
    for x in range(3, 2000000, 2):
        ps = filter(lambda b: (b <= int(x / 2)), primes)
        print('.', end='')
        start = time.time()
        if not divisible_by(x, *ps):
            primes.append(x)
            print(f"\nPrime: {x} found in {time.time() - start}sec")
    answer = sum(primes)
    print(f"{primes}\n\nProblem 10: {answer}")


problem10()
