elem1, elem2, elem3 = input()

el1 = int(elem1)
el2 = int(elem2)
el3 = int(elem3)

if el1 * 2 == el2 + el3 or el2 * 2 == el1 + el3 or el3 * 2 == el1 + el2:
    print("YES")
else:
    print("NO")
