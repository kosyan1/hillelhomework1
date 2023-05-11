name = input(str("Напишіть snake_case з трьох частин який переформатується в CapitalizedWords:"))
words = name.split('_')
upper_words = [word.capitalize() for word in words]
one_word = ''.join(upper_words)

print(f"Слово в форматі CapitalizedWords: {one_word}")
