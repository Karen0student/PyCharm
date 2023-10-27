from sys import stdin

my_list = []
for line in stdin:
    my_list.append(line.rstrip('\n')[:-1])

print(my_list)
