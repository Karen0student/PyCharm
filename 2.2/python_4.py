name1 = "Петя"
name2 = "Вася"
name3 = "Толя"
name1_speed = int(input())
name2_speed = int(input())
name3_speed = int(input())
mylist = [int(name1_speed), int(name2_speed), int(name3_speed)]
mylist.sort(reverse=True)
print(mylist)
index = 0
while index <= 2:
    if mylist[index] == name1_speed:
        print(f"{index + 1}. {name1}")
    elif mylist[index] == name2_speed:
        print(f"{index + 1}. {name2}")
    elif mylist[index] == name3_speed:
        print(f"{index + 1}. {name3}")
    index += 1


# if name1_speed > name2_speed and name1_speed > name3_speed:
#     print(name1)
# if name2_speed > name1_speed and name2_speed > name3_speed:
#     print(name2)
# if name3_speed > name1_speed and name3_speed > name2_speed:
#     print(name3)
