numbers = {1, 2, 3, 4, 5}
print({number: [number2 for number2 in range(1, number + 1) if number % number2 == 0] for number in numbers})
