numbers = [3, 1, 2, 3, 2, 2, 1]
print(' - '.join(str(digit) for digit in sorted({sorting_numbers for sorting_numbers in numbers})))
