transliteraciya = {
    'А': 'A', 'Б': 'B', 'В': 'V',
    'Г': 'G', 'Д': 'D', 'Е': 'E',
    'Ё': 'E', 'Ж': 'ZH', 'З': 'Z',
    'И': 'I', 'Й': 'I', 'К': 'K',
    'Л': 'L', 'М': 'M', 'Н': 'N',
    'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC',
    'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU',
    'Я': 'IA', 'Ь': '', 'Ъ': '',
}

main_list = []
with open("cyrillic.txt", encoding="UTF-8") as in_file:
    for line in in_file:
        main_list.append(line.rstrip("\n"))

in_file.close()

print_line = []
for index in range(len(main_list)):
    message_result = ""
    for word in main_list[index].split():
        for digit in word:
            if digit.upper() in transliteraciya:
                if digit.isupper():
                    message_result += transliteraciya[digit].lower().capitalize()
                else:
                    message_result += transliteraciya[digit.upper()].lower()
            else:
                message_result += digit
        message_result += " "
    print_line.append(message_result)

with open("transliteration.txt", "w", encoding="UTF-8") as output_file:
    print("\n".join(print_line), file=output_file)
output_file.close()

