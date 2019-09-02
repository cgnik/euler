# https://projecteuler.net/problem=22
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?
import string


def problem22():
    names = None
    with open("p022_names.txt") as f:
        names = f.read().replace('"', '').split(',')
        names.sort()
    letters = [' '] + [a for a in string.ascii_uppercase]

    def score(s):
        return sum(map(lambda x: letters.index(x), [a for a in s]))

    answer = []
    for i in range(0, len(names)):
        sc = score(names[i])
        answer.append(sc * (i + 1))
    print(f"Problem 22 answer: {sum(answer)}")


problem22()
