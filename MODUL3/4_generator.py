def index(text):
    seen = set()  # Хранилище для отслеживания уже встреченных букв
    result = []   # Список для хранения кортежей
    for i, char in enumerate(text):
        # Пропускаем пробелы и буквы, которые уже были обработаны
        if char.isspace() or char in seen or char == ".":
            continue
        seen.add(char)
        result.append((char, i))

    yield from sorted(result)

text = "The quick brown fox jumps over a lazy dog."
for letter, i in index(text):
    print(letter, i, sep="-", end=", ")
