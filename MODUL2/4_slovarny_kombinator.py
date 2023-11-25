string = input().split('; ')
quantity = int(input())


def generate_words(my_string, length):
    if length == 0:
        return ['']

    words = []
    for char in my_string:
        remaining_letters = [digit for digit in my_string if digit != char]
        words.extend([char + element for element in generate_words(remaining_letters, length - 1)])

    return words


result = sorted(set(generate_words(string, quantity)))
for word in result:
    print(word)
