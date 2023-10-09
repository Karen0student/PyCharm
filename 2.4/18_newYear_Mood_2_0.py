string, lengths = '', [0]
for j in range(1, (number := int(input())) + 1):
    string += str(j) + ' '
    if j in (sum(range(i)) for i in range(j + 2)):
        lengths.append(len(string) - 1)
        string = ''
lengths.append(len(string) - 1)
index = 1

for print_value in range(1, number + 1):
    if print_value - 1 in (sum(range(i)) for i in range(print_value + 2)):
        print(f"{' ' * ((max(lengths) - lengths[index]) // 2)}{print_value}", end=' ' if print_value != 1 else '\n')
        index += 1
    else:
        print(print_value, end='\n' if print_value in (sum(range(i)) for i in range(print_value + 2)) else ' ')
