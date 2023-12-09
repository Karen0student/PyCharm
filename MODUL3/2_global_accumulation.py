multiplication_parts_list = []


def add_number(number):
    multiplication_parts_list.append(number)


def get_prod():
    prev_mul_num = 1
    parts_to_str_list = []

    for number in multiplication_parts_list:
        prev_mul_num *= number
        parts_to_str_list.append(str(number))

    equation = " * ".join(parts_to_str_list)
    result = f"{equation} = {prev_mul_num}"

    return result


add_number(1)
add_number(2)
add_number(3)
print(get_prod())
