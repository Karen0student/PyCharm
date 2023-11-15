def merge(list_first: tuple, list_second: tuple) -> tuple:
    list_third = list(list_first) + list(list_second)
    # for index in range(len(list_third) - 2):
    #     if list_third[index] > list_third[index + 1]:
    #         tmp = list_third[index]
    #         list_third[index] = list_third[index + 1]
    #         list_third[index + 1] = tmp
    for i in range(len(list_third) - 1):
        for j in range(i + 1, len(list_third)):
            if list_third[i] > list_third[j]:
                tmp = list_third[i]
                list_third[i] = list_third[j]
                list_third[j] = tmp
    return tuple(list_third)


print(merge((1, 5, 3), (11, 12, 10)))
