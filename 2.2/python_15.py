name1 = "Петя"
name2 = "Вася"
name3 = "Толя"
name1_speed = int(input())
name2_speed = int(input())
name3_speed = int(input())
mylist = [int(name1_speed), int(name2_speed), int(name3_speed)]
mylist.sort(reverse=True)
index = 0
while index <= 2:
    if mylist[index] == name1_speed and index == 0:
        print(f"{name1:>14}")
    elif mylist[index] == name1_speed and index == 1:
        print(f"{name1:>6}")
    elif mylist[index] == name1_speed and index == 2:
        print(f"{name1:>22}")

    if mylist[index] == name2_speed and index == 0:
        print(f"{name2:>14}")
    elif mylist[index] == name2_speed and index == 1:
        print(f"{name2:>6}")
    if mylist[index] == name2_speed and index == 2:
        print(f"{name2:>22}")

    if mylist[index] == name3_speed and index == 0:
        print(f"{name3:>14}")
    elif mylist[index] == name3_speed and index == 1:
        print(f"{name3:>6}")
    elif mylist[index] == name3_speed and index == 2:
        print(f"{name3:>22}")
    index += 1

print(f"{'II':>5}{'I':>7}{'III':>9}")
