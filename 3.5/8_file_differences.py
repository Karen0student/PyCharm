file1_list = []
with open(f"{input()}", encoding="UTF-8") as file1:
    for line in file1:
        file1_list.append(line.rstrip("\n"))
file1.close()

file2_list = []
with open(f"{input()}", encoding="UTF-8") as file2:
    for line in file2:
        file2_list.append(line.rstrip("\n"))
file2.close()

# needed to split the lists
main_list = []
for index in range(len(file1_list)):
    tmp_list = file1_list[index].split()
    for element in tmp_list:
        main_list.append(element)
set1 = set(main_list)
main_list.clear()
for index in range(len(file2_list)):
    # main_list.append(file2_list[index].split())
    tmp_list = file2_list[index].split()
    for element in tmp_list:
        main_list.append(element)
set2 = set(main_list)
main_list.clear()
set3 = set1.symmetric_difference(set2)
# print("\n".join(set3))
set3 = sorted(set3)
print(set3)
with open(input(), "w", encoding="UTF-8") as file_answer:
    print("\n".join(set3), file=file_answer)
file_answer.close()


# second solution
# with open(input(), encoding='utf-8') as file1:
#     set1 = set(file1.read().split())
#
# with open(input(), encoding='utf-8') as file2:
#     set2 = set(file2.read().split())
#
# with open(input(), 'w', encoding='utf-8') as file:
#     answer_list = sorted(list(set1.symmetric_difference(set2)))
#     answer_line = '\n'.join(answer_list)
#     file.write(answer_line)

