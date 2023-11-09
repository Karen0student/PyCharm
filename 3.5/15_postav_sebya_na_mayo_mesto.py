import json
with open("scoring.json", encoding='utf-8') as file:
    data = json.load(file)
points = []
for group in data:
    for test in group['tests']:
        points.append({
            'pattern': str(test['pattern']),
            'points': group['points'] // len(group['tests'])
        })
result = 0
for val in points:
    if input() == val['pattern']:
        result += val['points']
print(result)
