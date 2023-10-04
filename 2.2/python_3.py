name1 = "Петя"
name2 = "Вася"
name3 = "Толя"
name1_speed = int(input())
name2_speed = int(input())
name3_speed = int(input())

if name1_speed > name2_speed and name1_speed > name3_speed:
    print(name1)
if name2_speed > name1_speed and name2_speed > name3_speed:
    print(name2)
if name3_speed > name1_speed and name3_speed > name2_speed:
    print(name3)
