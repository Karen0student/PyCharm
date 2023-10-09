quantity = int(input())
count = 0

for _ in range(quantity):
    string = input()
    words = string.split()
    for word in words:
        if "зайка" in word:
            count += 1
print(count)
