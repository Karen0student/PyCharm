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
# if len(set3) == 0:
#     print("Таких нет")
# else:
#     for elem in sorted(set3):
#         print(elem)
#
# # list1 = []
# # list2 = []
# #
# # for _ in range(Length1):
# #     list1.append(input())
# # for _ in range(Length2):
# #     list2.append(input())
# #
# # result = len(set(list1).difference(list2)) + len(set(list2).difference(list1))
# # if result == 0:
# #     print("Таких нет")
# # else:
# #     print_list = list1 + list2
# #     print_list.sort()
# #     print("\n".join(dict.fromkeys(print_list)))
# #

Length1 = int(input())
Length2 = int(input())

my_set = set()

for _ in range(Length1 + Length2):
    name = input()
    if name in my_set:
        my_set.discard(name)
    else:
        my_set.add(name)

if my_set:
    for name in sorted(my_set):
        print(name)
else:
    print("Таких нет")
