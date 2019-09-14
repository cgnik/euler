def nth(test, items):
    if test > 0:
        test -= 1
    else:
        test = 0
    for i, v in enumerate(items):
        if i == test: return v
