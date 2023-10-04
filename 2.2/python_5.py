name1 = "Петя"
name2 = "Вася"

name1_apple = 6
name2_apple = 9

number1 = int(input())
number2 = int(input())

name1_apple += number1
name2_apple += number2

if name1_apple > name2_apple:
    print(name1)
else:
    print(name2)
