import math
x_coordinate = float(input())
y_coordinate = float(input())
radius1 = 5
radius2 = 10
coord1 = math.sqrt((pow(x_coordinate, 2) + pow(y_coordinate, 2)))
coord2 = math.sqrt((pow(x_coordinate, 2) + pow(y_coordinate, 2)))
y_vert = (0.25 * (pow(x_coordinate, 2))) + (0.5 * x_coordinate) + 8.75

if x_coordinate >= 0 and y_coordinate >= 0:
    if coord1 <= radius1:
        print("Опасность! Покиньте зону как можно скорее!")
    elif coord2 > radius2:
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    else:
        print("Зона безопасна. Продолжайте работу.")
elif x_coordinate <= 0 and y_coordinate >= 0:
    # if y_coordinate <= 5 and y_coordinate <= ((5 * x_coordinate) + 35) / 3:
    if y_coordinate <= radius1 and y_coordinate <= ((radius1 * x_coordinate) + 35) / 3:
        print("Опасность! Покиньте зону как можно скорее!")
    elif coord2 > radius2:
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    else:
        print("Зона безопасна. Продолжайте работу.")
elif (x_coordinate >= 0 and y_coordinate <= 0) or (x_coordinate <= 0 and y_coordinate <= 0):
    if y_coordinate < y_vert:
        print("Опасность! Покиньте зону как можно скорее!")
    elif coord2 > radius2:
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    else:
        print("Зона безопасна. Продолжайте работу.")
elif x_coordinate == 0 and y_coordinate == 0:
    print("Опасность! Покиньте зону как можно скорее!")
