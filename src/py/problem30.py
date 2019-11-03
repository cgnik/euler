# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

from util.digit_exponents import power_sums


def problem30():
    limit = 10 ** 8
    print(f"calculating power sums with upper limit of {limit:,}")
    sums = list(power_sums(5, limit))
    print(f"Problem 30 found {len(sums)} sums of fifth powers {sums}")
    print(f"Problem 30: {sum(sums)}")


problem30()

# /home/christo/dev/euler/src/py/venv/bin/python /home/christo/dev/euler/src/py/problem30.py
# calculating power sums with upper limit of 10000000
# 100% complete.
# Problem 30 found 6 sums of fifth powers [4150, 4151, 54748, 92727, 93084, 194979]
# Problem 30: 443839
#
# Process finished with exit code 0