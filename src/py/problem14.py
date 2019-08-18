from util.collatz import collatz_series


def longest_collatz_between(start, end):
    answer = (0, [], 0)
    for i in range(start, end):
        if i % 1000 == 0: print('.', end='', flush=True)
        x = list(collatz_series(i))
        if len(x) > answer[2]:
            answer = (i, x, len(x))
    return answer


def problem14():
    answer = longest_collatz_between(13, 10 ** 6)
    print(f"Answer: {answer}")


problem14()
