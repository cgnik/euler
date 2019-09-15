# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
from util.repeats import unit_fraction_cycle

max_precision = 4096


def problem26():
    candidates = []
    print("Problem 26: Unit fraction cycles")
    for x in range(7, 1000):
        print(f"\rcalculating cycles: {int(x / 10)}%", end='', flush=True)
        cycle = unit_fraction_cycle(x, max_precision)
        if cycle != '':
            candidates.append((x, cycle))
    candidates = list(filter(lambda x: x[1] != '', candidates))
    candidates = [(len(c[1]), c[0], c[1]) for c in candidates]
    candidates.sort(reverse=True)
    print(f"\nCandidates(len {len(candidates)}): {candidates}")
    print(f"Problem 26 answer: {candidates[0]}")


problem26()
