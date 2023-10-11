string = input()
mylist = string.split()
divider = 1
result = divider
index = 0
min_of_mylist = int(min(mylist))
while divider != min_of_mylist + 1:
    if int(mylist[index]) % divider == 0 and index == len(mylist) - 1:
        result = divider
        index = 0
        divider += 1
        continue
    elif int(mylist[index]) % divider != 0:
        divider += 1
        index = 0
        continue
    if index == len(mylist) - 1:
        index = 0
        divider += 1
    index += 1

print(result)
