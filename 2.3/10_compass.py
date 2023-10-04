numberN = 0
numberE = 0
numberS = 0
numberW = 0

for _ in range(4):
    string = str(input())
    if string == "СТОП":
        break
    if string == "СЕВЕР":
        numberN = int(input())
    elif string == "ВОСТОК":
        numberE = int(input())
    elif string == "ЮГ":
        numberS = int(input())
    elif string == "ЗАПАД":
        numberW = int(input())

print(numberN - numberS)
print(numberE - numberW)
