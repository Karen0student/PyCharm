def number_length(number):
    result = str(number).replace("-", "")
    return len(result)


print(number_length("-12345"))
