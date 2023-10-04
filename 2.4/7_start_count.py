quantity = int(input())
count = 1
countdown = 3
while count <= quantity:
    for number in range(countdown, 0, -1):
        print(f"До старта {number} секунд(ы)")

    print(f"Старт {count}!!!")
    count += 1
    countdown += 1
