def to_string(*info, sep: str = " ", end: str = "\n"):
    if isinstance(info, tuple):
        my_list = [str(el) for el in info]
    else:
        my_list = info[0]

    string = ""
    for el in my_list:
        if el == my_list[len(my_list) - 1]:
            string += str(el) + end
        else:
            string += str(el) + sep

    return str(string)


print(to_string(1, 2, 3))
