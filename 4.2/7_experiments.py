my_list = []
odd = 0
couple = 0


def enter_results(*numbers):
    my_list.clear()
    sublist = [float(el) for el in numbers]
    for el in sublist:
        my_list.append(el)

    return my_list


def get_sum():
    for el in my_list:
        if el % 2 == 0:
            odd += float(el)
        else:
            couple += float(el)
    my_tuple = (sum(couple), sum(odd))
    return my_tuple


def get_average():
    odd = []
    count_odd = 0
    couple = []
    count_couple = 0
    for el in my_list:
        if el % 2 == 0:
            odd.append(el)
            count_odd += 1
        else:
            couple.append(el)
            count_couple += 1
    my_tuple = (float(format(sum(couple) / count_couple, ".2f")), float(format(sum(odd) / count_couple, ".2f")))
    return my_tuple


enter_results(1, 2, 3, 4, 5, 6)
print(get_sum(), get_average())
enter_results(1, 2)
print(get_sum(), get_average())
