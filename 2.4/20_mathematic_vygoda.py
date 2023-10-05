x = int(input())
number = x
max_sum = 0
optimal_base = 2

for base in range(2, 11):
    number = x
    current_sum = 0
    while number > 0:
        current_sum += number % base
        number //= base
    if current_sum > max_sum:
        max_sum = current_sum
        optimal_base = base
print(optimal_base)
