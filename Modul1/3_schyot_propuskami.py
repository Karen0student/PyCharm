number1 = int(input())
number2 = int(input())

for elem in range(number2, number1 + 1, (number2 - number1) % 10):
    if elem != number2:
        print(f", {elem}", end="")
    else:
        print(f"{elem}", end="")

# step = (number2 - number1) % 10
# print(number2, end=", ")
# while True:
#     number2 += step
#     if number2 == number1:
#         print(number2)
#         break
#     if number2 >= number1:
#         break
#     print(number2, end=", ")
