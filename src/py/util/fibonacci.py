def fibonacci():
    nums = [1, 1, 2]
    i = 3
    while True:
        index = i % 3
        nums[index] = nums[index - 2] + nums[index - 1]
        yield nums[index]
