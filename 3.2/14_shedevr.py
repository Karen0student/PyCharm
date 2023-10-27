quantity = int(input())
my_set = set()
meals = {}
for _ in range(quantity):
    my_set.add(input())

meal_num = int(input())
for _ in range(meal_num):
    meal_name = input()
    meal_num1 = int(input())
    for _ in range(meal_num1):
        meals.setdefault(meal_name, []).append(input())

list_of_foods = []
for food, ingredient in meals.items():
    if set(ingredient) <= my_set:
        list_of_foods.append(food)
if list_of_foods:
    for food in sorted(list_of_foods):
        print(food)
else:
    print("Готовить нечего")
