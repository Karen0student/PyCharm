N = int(input())
M = int(input())
Kotleta1 = int(input())
Kotleta2 = int(input())

result = (N * M - Kotleta2 * N) // abs(Kotleta1 - Kotleta2)
print(f'{result} {N - result}')
