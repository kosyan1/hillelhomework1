import string

def is_palindrome(sentence):
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    sentence = sentence.replace(" ", "").lower()
    reversed_sentence = sentence[::-1]
    return sentence == reversed_sentence

while True:
    vvod = input("Введіть речення: ")

    result = is_palindrome(vvod)

    print(f"Результат: {result}")
