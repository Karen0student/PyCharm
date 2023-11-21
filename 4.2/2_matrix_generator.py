def make_matrix(size, value=0):
    if isinstance(size, tuple):
        return [[value] * size[0] for _ in range(size[1])]
    else:
        return [[value] * size for _ in range(size)]


print(make_matrix((4, 2), 1))
