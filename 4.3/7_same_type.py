def same_type(f):

    def decorated(*args):
        if not all(isinstance(el, type(args[0])) for el in args):
            print("Обнаружены различные типы данных")
            return False
        return f(*args)
    return decorated


@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(7, '9') or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')
