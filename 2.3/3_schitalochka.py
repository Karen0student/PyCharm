number_start = int(input())
number_end = int(input())
result = []

while number_start != number_end + 1:
    result.append(str(number_start))
    number_start += 1

print(' '.join(result))
