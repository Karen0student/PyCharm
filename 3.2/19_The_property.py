quantity = int(input())
toys_dict = {}
for _ in range(quantity):
    line = input().split(": ")
    name = line[0]
    toys = line[1].split(", ")
    for toy in toys:
        toys_dict.setdefault(toy, set()).add(name)

private_list = []
for toy, names in toys_dict.items():
    if len(names) == 1:
        private_list.append(toy)
for toy in sorted(private_list):
    print(toy)
