my_list = []
with open(f"{input()}", encoding="UTF-8") as file:
    for line in file:
        my_list.append(line.rstrip("\n"))
file.close()
number_count = 0
greater_zero = 0
min_number = int(my_list[0][0])
max_number = int(my_list[0][0])
sum_of_all_numbers = 0
main_list = []
for index in range(len(my_list)):
    main_list.append(my_list[index].split())

for string in main_list:
    for number in string:
        number_count += 1
        if int(number) > 0:
            greater_zero += 1
        if int(number) < min_number:
            min_number = int(number)
        if int(number) > max_number:
            max_number = int(number)
        sum_of_all_numbers += int(number)

print(f"{int(number_count)}\n{int(greater_zero)}\n{int(min_number)}\n{int(max_number)}\n"
      f"{int(sum_of_all_numbers)}\n{float(sum_of_all_numbers / number_count):.2f}")
