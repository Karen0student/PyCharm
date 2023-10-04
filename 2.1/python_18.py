binary = int(input())
number2 = int(input())
number1 = 0
quantity_of_divisions = -1
while binary > 0:
    unit = binary % 10
    binary //= 10
    quantity_of_divisions += 1
    if unit != 0:
        res = pow(2, quantity_of_divisions)
        number1 += res

residual = number2 - number1
print(residual)
