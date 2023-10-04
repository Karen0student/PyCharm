def print_the_answer(side, sum_of_sides):
    if sum_of_sides == pow(side, 2):
        print("100%")
    elif sum_of_sides < pow(side, 2):
        print("велика")
    elif sum_of_sides > pow(side, 2):
        print("крайне мала")


side1 = int(input())
side2 = int(input())
side3 = int(input())

max_side = 1
maximum = side1
if maximum < side2:
    maximum = side2
    max_side = 2
if maximum < side3:
    maximum = side3
    max_side = 3

if max_side == 1:
    sides = pow(side2, 2) + pow(side3, 2)
    print_the_answer(side1, sides)
elif max_side == 2:
    sides = pow(side1, 2) + pow(side3, 2)
    print_the_answer(side2, sides)
elif max_side == 3:
    sides = pow(side1, 2) + pow(side2, 2)
    print_the_answer(side3, sides)



