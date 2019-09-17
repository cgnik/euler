from util.cartesian import all_factors


def abundant_numbers(up_to):
    abundants = []
    for n in range(12, up_to + 1):
        if n % 100 == 0: print(f"\rcalculating abundants: {int(n * 100 / up_to)}%", end='', flush=True)
        if sum(all_factors(n)) > n:
            abundants.append(n)
    abundants = list(set(abundants))
    abundants.sort()
    return abundants


def contains_sum_for(num, adders):
    adders = list(filter(lambda x: x < num, adders))
    adders.sort()
    start = 0
    end = len(adders) - 1
    if num in list(map(lambda n: n * 2, adders)):
        return True
    while start < end:
        result = adders[start] + adders[end]
        if result == num:
            return True
        elif result > num:
            end -= 1
        else:
            start += 1
    return False

# def contains_sum_for(num, adders):
#     available = [a for a in adders if a < num]
#     for index, a in enumerate(available):
#         if (num - a) in available:
#             return True
#     return False
