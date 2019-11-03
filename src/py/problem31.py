# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

coins = [1, 2, 5, 10, 20, 50, 100, 200]


def problem31():
    # need to figure out all permutations which sum to 200
    # maximum possible number of things in solution is 200, if they were all 1s
    # minimum possible number of things is 1, if it was just one 200
    # related to: number theory "partitions"
    answer = 0
    print(f"Problem 31: {answer}")


problem31()
