from sys import stdin
my_list = []

for line in stdin:
    my_list.append(line.rstrip("\n"))

printed_list_words = []

for index in range(len(my_list)):
    string = my_list[index].split()
    for word in string:
        if len(word) == 1:
            printed_list_words.append(word)
            continue
        flag = False
        first_index = 0
        for last_index in range(len(word) - 1, (len(word) - 1) // 2, -1):
            if word[first_index].lower() == word[last_index].lower():
                first_index += 1
                flag = True
            else:
                flag = False
                break
        if flag is True:
            printed_list_words.append(word)

print_set = set(printed_list_words)
print("\n".join(sorted(print_set)))
