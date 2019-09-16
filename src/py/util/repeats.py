import re, decimal

max_precision = 4096


def unit_fraction_cycle(n):
    decimal.setcontext(decimal.Context(prec=max_precision, rounding=decimal.ROUND_HALF_DOWN))
    val = str(decimal.Decimal(1) / decimal.Decimal(n))
    if val and '.' in val:
        s = val.split('.')[1][:-1]
        return repeats(s)
    return ''


def repeats(big_s):
    def find_repeats(s):
        l_str = len(s)
        l_max = int(l_str / 2)
        combos = []
        for start in range(0, l_max):
            combos.extend([s[start:end + start] for end in range(start, l_max + 1)])
        combos = set(combos)
        matches = [(len(re.findall(c, s)), len(c), (len(s) - s.index(c)), c) for c in combos if tip_to_tail(s, c)]
        matches.sort(reverse=True)
        if len(matches) > 0 and matches[0][0] > 1:
            return matches[0][3]
        return ''

    if len(big_s) > 1 and len(re.findall(big_s[0], big_s)) == len(big_s):
        return big_s[0]

    l_full = len(big_s)
    l_part = 16
    while l_part <= l_full:
        cycle = find_repeats(big_s[:l_part])
        if cycle != '' or l_part >= l_full:
            return cycle
        l_part *= 2
        l_part = min(l_part, l_full)
    return ''


def tip_to_tail(s, sub):
    if len(sub) == 0 or len(s) == 0:
        return False
    others = [o for o in s.split(sub)[1:] if o != sub and len(o) > 0]
    if len(others) > 0 and sub.startswith(others[-1]):
        others = others[:-1]
    return not len(others) > 0
