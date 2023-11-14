def split_numbers(number):
    my_list = number.split()
    return tuple(int(el) for el in my_list)


print(split_numbers("1 -2 3 -4 5"))
