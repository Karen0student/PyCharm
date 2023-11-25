import json

words = []
while True:
    word = input()
    word = word.lower()
    if not word:
        break
    words.append(word)

result_dict = {}
for word in words:
    for i in range(1, len(word), 2):
        letter = word[i]
        if letter not in result_dict:
            result_dict[letter] = []
        result_dict[letter].append(word)

for key in result_dict:
    result_dict[key] = sorted(set(result_dict[key]))

with open('result.json', 'w') as file:
    json.dump(result_dict, file, ensure_ascii=False, indent=2)
