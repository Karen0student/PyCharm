import math
string = input()
mylist = string.split()

number_degree = int(input())
for number in mylist:
    print(pow(int(number), number_degree), end=" ")
