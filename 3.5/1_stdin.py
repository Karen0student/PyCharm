from sys import stdin

my_list = []
for element in stdin:
    my_list.append(element.rstrip("\n"))

result = 0
for index in range(len(my_list)):
    split_list = my_list[index].split()
    for element in split_list:
        result += int(element)

print(result)
