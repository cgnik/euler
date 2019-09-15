import re
from decimal import Decimal


def unit_fraction_cycle(n):
    s = str(1 / Decimal(n)).split('.')[1][:-1]
    if len(s) >= 16:
        return repeats(s)
    return ''


def repeats(s):
    l_str = len(s)
    l_max = int(l_str / 2)
    combos = []
    # special exception for all same string
    if len(s) > 1 and len(re.findall(s[0], s)) == len(s):
        return s[0]
    for l in range(0, l_max):
        combos.extend([s[l:t] for t in range(l, l_max + 1)])
    combos = set(combos)
    print(f"Combos ({s}, max: {l_max}, l: {l_str}): {combos}")
    matches = [(len(re.findall(c, s)), len(c), (len(s) - s.index(c)), c) for c in combos if
               c != '' and tip_to_tail(s, c)]
    matches.sort(reverse=True)
    print(f"Matches ({s}): {matches}")
    if len(matches) > 0 and matches[0][0] > 1:
        return matches[0][3]
    return ''


def tip_to_tail(s, sub):
    others = [o for o in s.split(sub)[1:] if o != sub and len(o) > 0]
    if len(others) > 0 and sub.startswith(others[-1]):
        others = others[:-1]
    return not len(others) > 0
