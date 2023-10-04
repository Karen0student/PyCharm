import math
number1 = float(input())
number2 = float(input())
number3 = float(input())

if number1 == 0:
    if number2 == 0:
        if number3 == 0:
            print("Infinite solutions")
            exit(0)
        else:
            print("No solution")
            exit(0)
    else:
        x = -(number3 / number2)
        print(f"{x:.2f}")
        exit(0)

Diskriminant = pow(number2, 2) - (4 * number1 * number3)
if Diskriminant != 0 and Diskriminant > 0:
    x1 = (-number2 + math.sqrt(Diskriminant)) / (2 * number1)
    x2 = (-number2 - math.sqrt(Diskriminant)) / (2 * number1)
    print(f"{min(x1, x2):.2f} {max(x1, x2):.2f}")
elif Diskriminant >= 0:
    x = (-number2) // (2 * number1)
    print(f"{x:.2f}")
else:
    print("No solution")
