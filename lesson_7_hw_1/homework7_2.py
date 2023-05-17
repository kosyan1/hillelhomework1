import copy

while True:
    def correct_sentence(sentence):
        sentence_copy = copy.deepcopy(sentence)
        sentence_copy = sentence_copy.capitalize()
        if not sentence_copy.endswith('.'):
            sentence_copy += '.'
        return sentence_copy

    sentence = input("Введіть речення: ")

    result = correct_sentence(sentence)

    print(result)
