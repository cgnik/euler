num = 100000

x = [x * y for x in range(2, num) for y in range(2, num)]
x = list(filter(lambda z: z <= int(num / 2) and z > 0 and num % z == 0, x))
print(f"{x} : length:{len(x)}, sum:{sum(x)}")
