from math import gcd

numbers = set(input().split("; "))
numbers = [int(number) for number in numbers]
primes = {}
for number1 in numbers:
    for number2 in numbers:
        if number1 != number2 and gcd(number1, number2) == 1:
            primes.setdefault(number1, set()).add(number2)
for number in sorted(primes.keys()):
    if primes[number]:
        print(number, end=" - ")
        primes_line = ", ".join([str(c) for c in sorted(primes[number])])
        print(primes_line)
