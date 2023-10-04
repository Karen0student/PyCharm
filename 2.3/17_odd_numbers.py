number = input()
result_list = []
for i in range(len(number)):
    if int(number[i]) % 2 != 0:
        result_list.append(number[i])
print(''.join(result_list))
