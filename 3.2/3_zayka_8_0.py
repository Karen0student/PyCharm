# quantity = int(input())
# mylist = []
# for _ in range(quantity):
#     mylist.append(input())
#
# for index in range(len(mylist) - 1):
#     list1 = mylist[index].split()
#     list2 = mylist[index + 1].split()
#     print("\n".join(set(list1).difference(list2)))
#     # list1.clear()
    # list2.clear()


# result_list = []
#
# for index in range(len(mylist) - 1):
#     result_list.append(mylist[index].split())
#
# print_list = list(set(result_list))
# print(print_list)


mylist = []

for _ in range(int(input())):
    mylist.extend(input().split())

print("\n".join(set(mylist)))
