def popular_words(text, words):
    text_lower = text.lower()
    text_words = text_lower.split()

    result = {}

    for word in words:
        count = text_words.count(word)
        result[word] = count

    for word in words:
        if word not in result:
            result[word] = 0

    return result

while True:
    text = input("Введіть текст: ")
    words = input("Введіть слова, які потрібно знайти (через кому): ").split(",")

    cleaned_words = []

    for word in words:
        cleaned_word = word.strip().lower()
        cleaned_words.append(cleaned_word)

    result = popular_words(text, cleaned_words)

    print(result)
