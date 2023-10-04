first = int(input())
second = int(input())

m = first * second
while first != 0 and second != 0:
    if first > second:
        first %= second
    else:
        second %= first

print(m // (first + second))


