def gcd(first, second):
    while second != 0:
        first, second = second, first % second

    return first


print(gcd(int(input()), int(input())))
