numbers = input()
my_set = set()
numbers_list = numbers.split()
# for index in range(len(numbers_list)):
#     my_set.add(numbers_list[index])
# print(my_set)
# print(int(list(my_set)[0]) + 10)
flag_first = True
print(f"[")
# for elem in my_set:
for elem in numbers_list:
    elem = int(elem)
    digits = 0
    units = 0
    zeros = 0
    while elem >= 2:
        if elem % 2 == 0:
            elem //= 2
            zeros += 1
        else:
            elem //= 2
            #digits += 1
            units += 1
        #units += 1
        digits += 1

    #print("DIGITS: " + f"{digits}")
    #if elem == 1:
    units += 1
    digits += 1
    # else:
    #     zeros += 1
    #     digits += 1
    if flag_first is True:
        print(' ' * 4 + f"{'{'}\n" + ' ' * 8 + f"\"digits\": {digits},\n" + ' ' * 8 +
              f"\"units\": {units},\n" + ' ' * 8 + f"\"zeros\": {zeros}\n" + ' ' * 4 + f"{'}'}", end="")
        flag_first = False
    else:
        print(f",\n" + ' ' * 4 + f"{'{'}\n" + ' ' * 8 + f"\"digits\": {digits},\n" + ' ' * 8 +
              f"\"units\": {units},\n" + ' ' * 8 + f"\"zeros\": {zeros}\n" + ' ' * 4 + f"{'}'}", end="")
print(f"\n]")
