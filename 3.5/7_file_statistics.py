my_list = []
with open(f"{input()}", encoding="UTF-8") as file:
    for line in file:
        my_list.append(line.rstrip("\n"))

print(my_list)
number_count = 0
greater_zero = 0
min_number = my_list[0][0]
# print(int(min_number))
for string in my_list:
    for number in string:
        number_count += 1
        if int(number) > 0:
            greater_zero += 1

