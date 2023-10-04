A = int(input())
B = int(input())
speed = int(input())

Distance = B - A
hours = Distance / speed
#hours = round(hours, 2)
hours = "{:.2f}".format(hours)
print(hours)
