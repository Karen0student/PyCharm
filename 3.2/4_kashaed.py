Length1 = int(input())
Length2 = int(input())
list1 = []
list2 = []

for _ in range(Length1):
    list1.append(input())
for _ in range(Length2):
    list2.append(input())

sumOfSameElements = len(set(list1).intersection(list2))
if sumOfSameElements == 0:
    print("Таких нет")
else:
    print(sumOfSameElements)
