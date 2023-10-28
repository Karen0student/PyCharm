from sys import stdin
my_list = []
for line in stdin:
    my_list.append(line.rstrip("\n"))

target = my_list[-1]
target = target.lower()
for string in my_list:
    if string.lower() == target:
        break
    if target in string.lower():
        print(string)
