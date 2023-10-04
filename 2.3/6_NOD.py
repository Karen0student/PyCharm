first = int(input())
second = int(input())

while first != 0 and second != 0:
    if first > second:
        first %= second
    else:
        second %= first

print(first + second)
