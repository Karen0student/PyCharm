def is_palindrome(text):
    if isinstance(text, int):
        text = str(text)

    for index in range(len(text)):
        if text[index] != text[len(text) - index - 1]:
            return False

    return True


print(is_palindrome([1, 2, 1, 1]))
