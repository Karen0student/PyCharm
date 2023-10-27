meals = set()

quantity = int(input())
for i in range(quantity):
    meals.add(input())

day = int(input())
for i in range(day):
    meal_of_day = int(input())
    for j in range(meal_of_day):
        meals.discard(input())

if meals:
    for food in sorted(meals):
        print(food)
else:
    print("Готовить нечего")
