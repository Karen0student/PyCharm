quantity = int(input())
pair_list = []

for _ in range(quantity):
    pair_list.append((input(), input()))

name = pair_list[0][0]
max_number = 0
for index in range(len(pair_list)):
    number_sum = 0
    for digit in pair_list[index][1]:
        number_sum += int(digit)

    if max_number <= number_sum:
        max_number = number_sum
        name = pair_list[index][0]

print(name)

