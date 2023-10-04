guess = int(input())
number = 500
attempts = 0
residual = 500
while attempts < 10:
    answer = input()
    if number == guess:
        print("Угадал!")
        break
    if number < guess:
        print(number)
        print("Больше")
        if residual % 2 != 0:
            residual = (residual // 2) + 1
            number += residual
            attempts += 1
        else:
            residual //= 2
            number += residual
            attempts += 1
    else:
        print(number)
        print("Меньше")
        if residual % 2 != 0:
            residual = (residual // 2) + 1
            number -= residual
            attempts += 1
        else:
            residual //= 2
            number -= residual
            attempts += 1
