def result_accumulator(f):
    cash = []

    def decorated(*args, method="accumulate"):
        nonlocal cash
        if method != "drop":
            cash.append(f(*args))
            return None
        else:
            cash.append(f(*args))
            return_list = cash.copy()
            cash.clear()
            return return_list
    return decorated


@result_accumulator
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))
