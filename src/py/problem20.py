from functools import reduce


def problem20():
    fac = reduce(lambda x, accum: x * accum, range(1, 101))
    print(f"fac: {sum(map(int, list(str(fac))))}")


problem20()
