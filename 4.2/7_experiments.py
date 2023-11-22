my_list = []


def enter_results(*numbers):
    global my_list
    my_list.extend(list(numbers))


def get_sum():
    couple = 0
    odd = 0
    for index in range(len(my_list)):
        if index % 2 == 0:
            couple += my_list[index]
        else:
            odd += my_list[index]
    return round(couple, 2), round(odd, 2)


def get_average():
    couple = 0
    odd = 0
    for index in range(len(my_list)):
        if index % 2 == 0:
            couple += my_list[index]
        else:
            odd += my_list[index]
    count_of_elements = len(my_list) / 2
    avg1 = round(couple / count_of_elements, 2)
    avg2 = round(odd / count_of_elements, 2)
    return avg1, avg2


enter_results(3.5, 2.14, 45.2, 37.99)
print(get_sum(), get_average())
enter_results(5.2, 7.3)
print(get_sum(), get_average())
enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
print(get_sum(), get_average())
