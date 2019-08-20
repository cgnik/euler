from num2words import num2words


def problem17():
    print(f"Problem 17: {sum([len(num2words(a).replace(' ', '').replace('-', '')) for a in range(1,1001)])}")


problem17()
