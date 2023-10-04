quantity = int(input())
all_lists = []
for _ in range(quantity):
    sublist = []
    while True:
        string = input()
        if string == "ВСЁ":
            break
        sublist.append(string)
    all_lists.append(sublist)

answer_quantity = 0
for index in range(quantity):
    if "зайка" in all_lists[index]:
        answer_quantity += 1
        continue

print(answer_quantity)
