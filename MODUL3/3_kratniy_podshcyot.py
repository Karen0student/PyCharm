def count_pairs(*numbers, div=10):
    quantity = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j]) % div == 0:
                quantity += 1
    return quantity


numbers = [41, 56, 54, 6, 31, 81, 77, 83, 86, 15]
result = count_pairs(*numbers, div=3)
print(result)
