quantity = int(input())
menu_list = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
index = 0
flag_value = 5
for number in range(quantity):
    if number >= flag_value:
        index -= 5
        flag_value += 5
    print(menu_list[index])
    index += 1
