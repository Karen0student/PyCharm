mylist = []
while True:
    string = input()
    if string == "ФИНИШ":
        break
    else:
        mylist.append(string)

digit_list = {}

for word in mylist:
    for digit in word:
        if digit == ' ':
            continue
        digit = digit.lower()
        if digit in digit_list:
            digit_list[digit] += 1
        else:
            digit_list[digit] = 1
max_quantity_word = ''
max_value = 0
for key, value in digit_list.items():
    if max_value < value:
        max_value = value
        max_quantity_word = key
print(max_quantity_word)
# digit_list = sorted(digit_list)
# print(digit_list[0].lower())

# digit_list = []
# for word in mylist:
#     for digit in word:
#         if digit == ' ':
#             continue
#         # digit = digit.lower()
#         if digit in digit_list:
#             continue
#         else:
#             digit_list.append(digit)
#
# quantity_list = []
# for digit in digit_list:
#     quantity_list.append(mylist.count(digit))
#
# index = quantity_list.index(max(quantity_list))
# print(digit_list[index])
