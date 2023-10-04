side1, side2, side3 = input()
side1 = int(side1)
side2 = int(side2)
side3 = int(side3)

if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
    print("YES")
else:
    print("NO")

