from util.cartesian import all_factors


def abundant_numbers(up_to):
    abundants = []
    for n in range(12, up_to):
        if n % 100 == 0: print(f"\r{int(n * 100 / up_to)}%", end='', flush=True)
        if sum(all_factors(n)) > n:
            abundants.append(n)
    return abundants
