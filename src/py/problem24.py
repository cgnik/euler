# Lexicographic permutations
#
# Problem 24
#
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
from util.permutation import permutations


def problem24():
    p = [''.join(p) for p in permutations([str(n) for n in range(0, 10)]) if p[0] in "012"]
    p.sort()
    print(f"Problem 24: Millionth permutation sorted lexically (total count {len(p)}): {p[999999]}")


problem24()
