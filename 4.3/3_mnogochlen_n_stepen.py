def make_equation(*my_number_list):
    if len(my_number_list) <= 1:
        return my_number_list[0]
    else:
        return f"({make_equation(*my_number_list[0:-1])}) * x + {my_number_list[-1]}"


print(make_equation(3, 1, 5, 3))
