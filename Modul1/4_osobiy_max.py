quantity = int(input())
Biggest_number = float('-inf')
previous_number = int(input())  # первый элемент
for _ in range(quantity - 1):
    elem = int(input())
    if elem < previous_number:
        Biggest_number = max(elem, Biggest_number)
        
    previous_number = elem

print(Biggest_number)
