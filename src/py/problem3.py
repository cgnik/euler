from math import sqrt
from time import gmtime, strftime


def factors(num):
    factor = int(sqrt(num))
    print(f"starting factorization with {factor}")
    while factor % 2 == 0:
        factor = int(factor / 2)
    while num > 1:
        if num % factor == 0:
            yield factor
            num = int(num/factor)
        factor -= 2
    yield num


if __name__ == '__main__':
    # num = 1234141233
    num = 600851475143
    fs = [f for f in factors(num)]
    fs.append([x for f in x for x in factors(f)])
    print(f"{fs}")