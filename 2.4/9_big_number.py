quantity = int(input())
mylist = []
for _ in range(quantity):
    mylist.append(input())

max_digits_list = []
for index in range(len(mylist)):
    digits_list = []
    for digit in mylist[index]:
        digits_list.append(digit)
    digits_list = sorted(digits_list, reverse=True)
    max_digits_list.append(digits_list[0])

print(''.join(max_digits_list))
