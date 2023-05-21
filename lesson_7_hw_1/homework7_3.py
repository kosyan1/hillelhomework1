while True:
    def second_index(words, target):
        index_1 = words.find(target)
        if index_1 == -1:
            return None
        else:
            index_2 = words.find(target, index_1 + 1)
            if index_2 == -1:
                return None
            return index_2
    words = input("Введіть рядок слів: ")
    target = input("Введіть значення, по якому потрібно знайти індекс другого входження в рядку слів: ")

    result = second_index(words, target)
    print(result)
