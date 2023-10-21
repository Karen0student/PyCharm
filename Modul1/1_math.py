import math
first = int(input())
second = int(input())
third = int(input())

print(f"{first} ^ ({second} mod {third}) = {pow(first, second % third)}")
