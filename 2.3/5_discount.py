number_list = []
while True:
    number = float(input())
    if number == 0:
        break
    number_list.append(number)

result = 0
for element in number_list:
    if element >= 500:
        element = element * 0.9
    result += element

print(result)
