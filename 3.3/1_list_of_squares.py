string1 = input()
string2 = input()
number1 = int(string1[3:])
number2 = int(string2[3:])

my_list = []
while number1 <= number2:
    my_list.append(number1 * number1)
    number1 += 1

print(my_list)
