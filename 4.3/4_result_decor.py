def answer(f):
    def decorated(*args, **kwargs):
        result = f(*args, **kwargs)
        return f"Результат функции: {result}"
    return decorated


@answer
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5))
print(a_plus_b(7, 9))
