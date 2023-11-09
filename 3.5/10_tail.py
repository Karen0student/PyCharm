path = input()
num_lines = int(input())
with open(path, encoding='utf-8') as file1:
    lines = file1.readlines()
    if len(lines) < num_lines:
        num_lines = len(lines)
    for line in lines[-num_lines:]:
        print(line, end='')
