def bunny(start, finish, length):
    jmp_ways = []

    def generate_paths(current_path, rem_jmps):
        if current_path[-1] == finish and rem_jmps != 0:
            return
        if rem_jmps == 0:
            if current_path[-1] == finish:
                jmp_ways.append(current_path.copy())
            return

        for step in [-3, -1, 1, 3]:
            next_position = current_path[-1] + step
            current_path.append(next_position)
            generate_paths(current_path, rem_jmps - 1)
            current_path.pop()

    generate_paths([start], length)
    return jmp_ways


result = bunny(7, 10, 3)
print(*result, sep="\n")
