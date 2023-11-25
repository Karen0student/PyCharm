word_dict = {}

while True:
    line = input()
    if not line:
        break
    words = line.split()
    for word in words:
        length = len(word)
        middle_char = word[length // 2 - 1].lower() if length % 2 == 0 else word[length // 2].lower()
        if middle_char not in word_dict:
            word_dict[middle_char] = set()
        word_dict[middle_char].add(word.upper())

for key in sorted(word_dict.keys()):
    words_str = ". ".join(sorted(word_dict[key]))
    print(f"{key} \"{words_str}\"")
