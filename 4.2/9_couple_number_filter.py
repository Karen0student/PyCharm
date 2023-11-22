# numbers = (32, 64, 128, 256, 512)
# filter_even_digit_sum = lambda num: sum(int(digit) for digit in str(num)) % 2 == 0
# filtered_numbers = list(filter(filter_even_digit_sum, numbers))
# print(" ".join([str(el) for el in filtered_numbers]))
print(*filter(lambda num: sum(int(digit) for digit in str(num)) % 2 == 0, (1, 2, 3, 4, 5)))
