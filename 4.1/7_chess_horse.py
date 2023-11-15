def can_eat(first, second):
    if first[0] + 2 == second[0] or first[0] - 2 == second[0]:
        if first[1] + 1 == second[1] or first[1] - 1 == second[1]:
            return True
    elif first[0] + 1 == second[0] or first[0] - 1 == second[0]:
        if first[1] + 2 == second[1] or first[1] - 2 == second[1]:
            return True
    return False


print(can_eat((5, 5), (6, 6)))

