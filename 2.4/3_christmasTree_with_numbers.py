number = int(input())
quantity = 0
stage = 1
for i in range(1, number + 1):
    print(f"{i} ", end="")
    quantity += 1
    if quantity == stage:
        quantity = 0
        stage += 1
        print('')
