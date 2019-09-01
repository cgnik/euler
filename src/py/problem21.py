from util.factoring import all_factors


# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

def problem21():
    all = {}
    for i in range(2, 10000):
        if i % 100 == 0:
            print('.', end='', flush=True)
        all[i] = sum(all_factors(i))
    answer = []
    print(f"\n{all}\nsumming...")
    for k, v in all.items():
        if k != v and v in all and v == all[v]:
            answer.append(((k, all[k]), (v, all[v])))
    print(f"Answer ({len(answer)}): {answer}")


problem21()
