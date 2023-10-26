# Length1 = int(input())
# Length2 = int(input())
# set1 = set()
# set2 = set()
# for _ in range(Length1):
#     set1.add(input())
# for _ in range(Length2):
#     set2.add(input())
#
# set3 = set1.symmetric_difference(set2)
# set3 = list(set(set3))
# if len(set3) == 0:
#     print("Таких нет")
# else:
#     print(len(set3))
#
#
# # list1 = []
# # list2 = []
# #
# # for _ in range(Length1):
# #     list1.append(input())
# # for _ in range(Length2):
# #     list2.append(input())
# #
# # sumOfSameElements = len(set(list1).intersection(list2)) + len(set(list2).intersection(list1))
# # if (Length1 + Length2) - sumOfSameElements == 0:
# #     print("Таких нет")
# # else:
# #     print((Length1 + Length2) - sumOfSameElements)

Length1 = int(input())
Length2 = int(input())

my_set = set()

for _ in range(Length1 + Length2):
    name = input()
    if name in my_set:
        my_set.discard(name)
    else:
        my_set.add(name)

quantity_of_names = len(my_set)
print(quantity_of_names if quantity_of_names else "Таких нет")
