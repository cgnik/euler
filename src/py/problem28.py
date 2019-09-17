# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

from util.spiral import spiral_diagonals


def problem28():
    values = spiral_diagonals(1001)
    # think it should be 2001 count of integers, given width of 1001
    # should have a list of 2n-1 integers (by count), considering the 5x5 example
    print(f"values: {', '.join([str(v) for v in values])}")
    print(f"Problem 28: sum: {sum(values)}, count: #{len(values)}")


problem28()
