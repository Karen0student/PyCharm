string = input()
print(sorted(string.split(), key=lambda x: (len(x), x.lower())))
