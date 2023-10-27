quantity = int(input())
meal = {}

for _ in range(quantity):
    item = input().split()
    for food in item[1:]:
        meal.setdefault(food, []).append(item[0])
if (food := input()) in meal:
    for kid in sorted(meal[food]):
        print(kid)
else:
    print("Таких нет")
