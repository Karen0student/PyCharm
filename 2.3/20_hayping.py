number = int(input())
prevHash = 0
for i in range(number):
    block = int(input())
    x = block // (256 ** 2)
    y = (block // 256) % 256
    currHash = (37 * (y + x + prevHash)) % 256
    if currHash >= 100 or currHash != block % 256:
        print(f"\n{i}")
        break
    prevHash = currHash
else:
    print(-1)

