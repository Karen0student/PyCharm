string_check = []


def modern_print(string):
    if string not in string_check:
        string_check.append(string)
        print(string)


modern_print("Name")
modern_print("Name")
