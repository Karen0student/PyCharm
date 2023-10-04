number = int(input())
for multiplier in range(1, number + 1):
    for i in range(1, number + 1):
        first_number = i
        print(f"{first_number} * {multiplier} = {first_number * multiplier}")
    multiplier += 1
