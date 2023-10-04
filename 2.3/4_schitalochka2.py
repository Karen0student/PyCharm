number_start = int(input())
number_end = int(input())
result = []
if number_start < number_end:
    while number_start != number_end + 1:
        result.append(str(number_start))
        number_start += 1
elif number_start == number_end:
    print(number_start)
else:
    while number_start != number_end - 1:
        result.append(str(number_start))
        number_start -= 1

print(' '.join(result))
