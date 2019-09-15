import re


def unit_fraction_cycle(n):
    return repeats(str(1 / n).split('.')[1])


def repeats(s):
    m = ''
    x_len = len(s)
    if len(s) >= 16:
        for i in reversed(range(0, int(len(s) / 2))):
            sub = s[i:-1]
            match_count = len(re.findall(sub, s))
            if match_count > 1:
                m = sub
                break
    return m
