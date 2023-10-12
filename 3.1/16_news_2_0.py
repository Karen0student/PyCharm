Length = int(input())
quantity = int(input())
mylist = []

for _ in range(quantity):
    mylist.append(input())

digit_count = 0
for string in mylist:
    if digit_count + len(string) < Length - 3:
        print(string)
        digit_count += len(string)
    else:
        print_length = Length - digit_count - 3
        print(f"{string[:Length - digit_count - 3]}...")
        break
