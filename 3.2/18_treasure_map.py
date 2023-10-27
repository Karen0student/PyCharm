quantity = int(input())
treasures = {}
for _ in range(quantity):
    coordinates = input().split()
    last_digits = f'{coordinates[0][:-1]}-{coordinates[1][:-1]}'
    treasures[last_digits] = treasures.setdefault(last_digits, 0) + 1
maximum_value = max(treasures.values())
print(maximum_value)
