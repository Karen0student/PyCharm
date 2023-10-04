# quantity = int(input())
# mylist = []
# for _ in range(quantity):
#     mylist.append(int(input()))
#
# nod_list = []
# for index in range(len(mylist) - 1):
#     nod_list.append(math.gcd(mylist[index], mylist[index + 1]))
#
# nod_list = sorted(nod_list)
# print(nod_list)
# print(nod_list[0])
# while first != 0 and second != 0:
#     if first > second:
#         first %= second
#     else:
#         second %= first
#
# print(first + second)


#EXAMPLE
#4 4 8 12 9
import math

quantity = int(input())
mylist = []
for _ in range(quantity):
    mylist.append(int(input()))

nod_coefficient = math.gcd(math.gcd(mylist[0], mylist[1]))
if quantity == 2:
    print(nod_coefficient)
    exit(0)
else:
    index = 2
    while True:
        if nod_coefficient == 1 or index > len(mylist) - 1:
            break
        if mylist[index] % nod_coefficient != 0:
            nod_coefficient -= 1
            index = 0
        else:
            index += 1
print(nod_coefficient)
