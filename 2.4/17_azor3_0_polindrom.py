quantity = int(input())
count = 0
for i in range(quantity):
    number = input()
    is_pol = True
    for index in range((len(number) // 2)):
        if number[index] != number[len(number) - 1 - index]:
            is_pol = False
            break
    if is_pol is True:
        count += 1

print(count)
