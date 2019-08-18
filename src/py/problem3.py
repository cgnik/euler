from util.factoring import factors

if __name__ == '__main__':
    num = 600851475143
    fs = [f for f in factors(num)]
    fs.append([x for f in x for x in factors(f)])
    print(f"{fs}")
