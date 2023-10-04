count = 0
quantity = int(input())
for _ in range(quantity):
    string = str(input())
    if "зайка" in string:
        count += 1
print(count)
