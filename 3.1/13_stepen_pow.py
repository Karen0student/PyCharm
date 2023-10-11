import math
quantity = int(input())
number_list = []
for _ in range(quantity):
    number_list.append(int(input()))

number_degree = int(input())
for number in number_list:
    print(pow(number, number_degree))
