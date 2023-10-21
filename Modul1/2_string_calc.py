string = input()
number1 = int(input())
number2 = int(input())

if "sum" in string:
    print(number1 + number2)
elif "sub" in string:
    print(number1 - number2)
elif "mult" in string:
    print(number1 * number2)
elif "div" in string:
    print(number1 // number2)
