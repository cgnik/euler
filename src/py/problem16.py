from functools import reduce

def problem16():
    print(f"Problem 16 {reduce(lambda x,y: x+y, [int(a) for a in str(2**1000)])}")


problem16()
