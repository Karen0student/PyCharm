def gcd(*numbers):
    if isinstance(numbers, int):
        return numbers

    gcd_result = numbers[0]

    for num in numbers[1:]:
        while num:
            gcd_result, num = num, gcd_result % num

    return gcd_result


# Example usage
result_gcd = gcd(36, 48, 156, 100500)

print(result_gcd)
