my_list = []
while True:
    string = input()
    if string == "":
        break
    my_list.append(string)

main_list = []

for elem in my_list:
    main_list.append(elem.split())

my_list.clear()

for group in main_list:
    if "зайка" in group:
        for index in range(len(group) - 1):
            if group[index] == "зайка":
                my_list.append(group[index + 1])
                my_list.append(group[index - 1])
my_set = set(my_list)
print("\n".join(sorted(my_set)))
