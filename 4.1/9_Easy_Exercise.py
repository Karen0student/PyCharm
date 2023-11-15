from math import sqrt


def is_prime(number):
    #  for divider in range(2, number // 2):
    for divider in range(2, int(sqrt(number)) + 1):
        if number % divider == 0:
            return False
    return True


print(is_prime(1001459))
