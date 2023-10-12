string = input()

number_str1 = string[0]
count = 0
for number_str2 in string:
    if number_str1 == number_str2:
        count += 1
    else:
        print(f"{number_str1} {count}")
        count = 1
        number_str1 = number_str2

print(f"{number_str1} {count}")
