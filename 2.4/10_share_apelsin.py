quantity = int(input())

print("A B C")
for A in range(1, quantity - 1, 1):
    B = 1
    C = quantity - A - B
    while C >= 1:
        print(f"{A} {B} {C}")
        C -= 1
        B += 1
