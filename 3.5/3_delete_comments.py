from sys import stdin
my_list = []
for line in stdin:
    my_list.append(line.rstrip("\n"))
print()
for string in my_list:
    for word in string:
        if string[0] == "#":
            break
        if word == "#":
            if string != my_list[-1]:
                print()
            break
        else:
            print(word, end="")
    #if string != my_list[-1]:
