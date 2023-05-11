while True:
    import string

    vvod = input("Введіть дві букви через дефіз: ")
    start, end = vvod.split('-')

    all_string = string.ascii_letters
    start_index = all_string.index(start)
    finish_index = all_string.index(end)

    new_string = all_string[start_index:finish_index + 1]
    print(new_string)
