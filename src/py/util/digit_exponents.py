def is_power_sum(n, exponent):
    return sum(map(lambda x: int(x) ** exponent, str(n))) == n


def power_sums(exponent, limit=10000):
    n = 1
    one_percent = int(limit / 100)
    percent_complete = 0
    while n <= limit:
        if int((n / limit) * 100) > percent_complete:
            percent_complete = int((n / limit) * 100)
            print(f"\r{percent_complete}% complete...", flush=True, end='')
        n += 1
        if is_power_sum(n, exponent):
            yield n
    print("\r100% complete.")
