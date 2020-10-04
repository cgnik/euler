# https://projecteuler.net/problem=33
#
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
from functools import reduce
from operator import mul

all_nums = [f"{x}" for x in range(11, 100) if x % 10 != 0]


def problem33():
    combos = [(a, b) for a in all_nums for b in all_nums]
    answers = []
    for i in range(1, 10):
        si = f"{i}"
        for x, y in list(filter(lambda z: si in f"{z[0]}" and si in f"{z[1]}", combos)):
            if x == y or x.strip(si) == '' or y.strip(si) == '': continue
            p, d = float(f"{x}".strip(si)), float(f"{y}".strip(si))
            if (p / d) > 1: continue
            if (float(x) / float(y)) == (p / d):
                answers.append((x, y))
    n, d = [int(n[0]) for n in answers], [int(n[1]) for n in answers]
    pn, pd = reduce(mul, n), reduce(mul, d)
    print(f"numerator: {pn} denominator: {pd} Done.")


problem33()
