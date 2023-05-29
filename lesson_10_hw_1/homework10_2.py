def first_word(text):
    word = ''
    for symbol in text:
        if symbol.isalpha() or symbol == "'":
            word += symbol
        elif word:
            break

    return word

while True:
    text = input("Введіть рядок: ")

    result = first_word(text)

    print(result)
