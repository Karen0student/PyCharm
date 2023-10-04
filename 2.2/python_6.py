number = int(input())

if number % 4 == 0 and number % 100 != 0:
    print("YES")
elif number % 1000 == 0:
    print("YES")
else:
    print("NO")
