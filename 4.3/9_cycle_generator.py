def cycle(lst):
    if not lst:
        return

    index = 0
    while True:
        yield lst[index]
        index = (index + 1) % len(lst)


# Пример использования:
print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))
