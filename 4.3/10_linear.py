def make_linear(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(make_linear(item))
        else:
            result.append(item)
    return result


# Пример использования:
nested_list = [1, 2, [3, 4, [5, 6]], 7, [8]]
linear_list = make_linear(nested_list)
print(linear_list)
