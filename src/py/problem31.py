# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

# https://en.wikipedia.org/wiki/Partition_(number_theory)
# these are the "partitions" of 200, and so predicted by a partition function
# no closed form of the function is known
def make_change(amount, coins):
    counts = [0] * (amount + 1)
    # have to initialize with 1 as 'seed'
    counts[0] = 1 # p(0) === 1
    for coin in coins:
        for i in range(coin, len(counts)):
            counts[i] = counts[i] + counts[i - coin]
        print(f"DEBUG: coin/index/counts: {coin}/{counts}")
    return counts[-1]


def change_largest_coin(coins):
    return make_change(max(coins), coins)


def problem31_american():
    print(f"Problem 31 American: {change_largest_coin([1, 5, 10, 25, 50, 100])}")


def problem31_english():
    print(f"Problem 31 English: {change_largest_coin([1, 2, 5, 10, 20, 50, 100, 200])}")


def problem31():
    print(f"Problem 31 test: 12: {make_change(12, [1, 2, 5])}")
    print(f"Problem 31 test: 10: {change_largest_coin([1, 5, 10])}")
    problem31_american()
    problem31_english()


problem31()
