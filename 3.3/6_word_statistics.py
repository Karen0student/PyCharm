text = 'Мама мыла раму!'
print({char: text.lower().count(char) for char in text.lower() if char.isalpha()})
