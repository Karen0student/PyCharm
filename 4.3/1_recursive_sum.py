def recursive_sum(*number):
    if not number:
        return 0
    else:
        return number[0] + recursive_sum(*number[1:])


print(recursive_sum(7, 1, 3, 2, 10))
