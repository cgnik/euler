import re
from decimal import Decimal


def unit_fraction_cycle(n):
    val = str(1 / Decimal(n))
    if val and '.' in val:
        s = val.split('.')[1][:-1]
        if len(s) >= 16:
            return repeats(s)
    return ''


def repeats(s):
    l_str = len(s)
    l_max = int(l_str / 2)
    combos = []
    if len(s) > 1 and len(re.findall(s[0], s)) == len(s):
        return s[0]
    for start in range(0, l_max):
        combos.extend([s[start:end + start] for end in range(start, l_max + 1)])
    combos = set(combos)
    matches = [(len(re.findall(c, s)), len(c), (len(s) - s.index(c)), c) for c in combos if tip_to_tail(s, c)]
    matches.sort(reverse=True)
    if len(matches) > 0 and matches[0][0] > 1:
        return matches[0][3]
    return ''


def tip_to_tail(s, sub):
    if len(sub) == 0 or len(s) == 0:
        return False
    others = [o for o in s.split(sub)[1:] if o != sub and len(o) > 0]
    if len(others) > 0 and sub.startswith(others[-1]):
        others = others[:-1]
    return not len(others) > 0
