import json
with open(input(), encoding='utf-8') as file:
    s = [int(x) for x in file.read().split()]
count_greater = 0
for x in s:
    if x > 0:
        count_greater += 1
count = len(s)
sum_of_all = sum(s)
result = {
    'count': count,
    'positive_count': count_greater,
    'min': min(s),
    'max': max(s),
    'sum': sum_of_all,
    'average': round(sum_of_all / count, 2)
}
with open(input(), 'w', encoding='utf-8') as into_file:
    json.dump(result, into_file, indent=4, separators=(', ', ': '))
