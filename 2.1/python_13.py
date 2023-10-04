number1 = int(input())
number2 = int(input())

char1 = (number1 // 100 + number2 // 100) % 10
char2 = (number1 // 10 % 10 + number2 // 10 % 10) % 10
char3 = (number1 % 10 + number2 % 10) % 10
print(f"{char1}{char2}{char3}")
