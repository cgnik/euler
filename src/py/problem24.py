# Lexicographic permutations
#
# Problem 24
#
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def swap(arr1, index1, arr2, index2):
    x = arr1[index1]
    arr1[index1] = arr2[index2]
    arr2[index2] = x


def heap(c):
    i
    while i < len(c):
        if c[i] < i:
            if i % 2 == 0:
                swap(A, 0, A, i)
            else:
                swap(A[c[i]], A[i])
            print(A)
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1


def problem24():
    generate([str(n) for n in range(0, 10)])


problem24()
