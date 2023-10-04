guess = 123
number = 500
attempts = 0
residual = 500
while attempts < 10:
    print(number)
    answer = input()
    if answer == "Угадал!":
        print("Число отгадано")
        break
    if answer == "Больше":
        if residual % 2 != 0:
            residual = (residual // 2) + 1
            number += residual
            attempts += 1
        else:
            residual //= 2
            number += residual
            attempts += 1
    elif answer == "Меньше":
        if residual % 2 != 0:
            residual = (residual // 2) + 1
            number -= residual
            attempts += 1
        else:
            residual //= 2
            number -= residual
            attempts += 1
