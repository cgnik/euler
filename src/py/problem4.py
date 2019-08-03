from util import find_palindromes


def first(x): return x[0]


def problem4():
    palindromes = find_palindromes()
    palindromes.sort(key=first, reverse=True)
    print(f"best: {palindromes[0]}")


problem4()
