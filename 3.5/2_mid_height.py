from sys import stdin

my_list = []
for line in stdin:
    my_list.append(line.rstrip("\n"))

list_names = []
height_differences = 0
for index in range(len(my_list)):
    split_list = my_list[index].split()
    if split_list[0] not in list_names:
        list_names.append(split_list[0])
        first_height = int(split_list[1])
        second_height = int(split_list[2])
        height_differences += second_height - first_height

print(round(height_differences / len(my_list)))
