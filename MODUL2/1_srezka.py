# def process_package(N, packages):
#     result = []
#
#     for i in range(N):
#         package = packages[i].split('^')
#         s = package[0]
#         a, b = map(int, package[1:])
#
#         # Вычислить шаг среза
#         step = len(s) % 4
#
#         # Взять срез строки от A до B с шагом step
#         sliced_string = s[a:b:step]
#
#         # Добавить срез в результат
#         result.append(sliced_string)
#
#     return result
#
#
# quantity = int(input())
# my_packages = [input() for _ in range(quantity)]
# final_result = process_package(quantity, my_packages)
# for line in final_result:
#     print(line)


quantity = int(input())

for _ in range(quantity):
    my_package = input()
    package_block = my_package.split('^')
    a, b = int(package_block[1]), int(package_block[2])
    step = len(package_block[0]) % 4
    result = package_block[0][a:b:step]

    print(result)
