def is_palindrome(x):
    s = str(x)
    end = len(s) - 1
    for i in range(0, len(s)):
        if s[i] != s[end - i]:
            return False
    return True


def find_palindromes():
    all = []
    for i in range(100, 999):
        for j in range(100, 999):
            if is_palindrome(i * j):
                all.append((i * j, i, j))
    return all


def first(x): return x[0]


def do_thing():
    palindromes = find_palindromes()
    palindromes.sort(key=first, reverse=True)
    print(f"best: {palindromes[0]}")


do_thing()
