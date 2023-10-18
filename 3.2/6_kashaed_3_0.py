Length1 = int(input())
Length2 = int(input())
list1 = []
list2 = []

for _ in range(Length1):
    list1.append(input())
for _ in range(Length2):
    list2.append(input())

result = len(set(list1).difference(list2)) + len(set(list2).difference(list1))
if result == 0:
    print("Таких нет")
else:
    print_list = list1 + list2
    print_list.sort()
    print("\n".join(dict.fromkeys(print_list)))

