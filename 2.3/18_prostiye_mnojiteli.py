number = int(input())
result = []
divider = 2
while number != 1:
    if number % divider != 0:
        divider += 1
    else:
        result.append(str(divider))
        number //= divider

print(' * '.join(result))
