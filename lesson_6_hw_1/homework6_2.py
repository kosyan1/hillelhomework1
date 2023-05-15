while True:
    dct = {}
    lst = input("Введіть рядок, з якого потрібно зробити словник: ")

    for el in lst:
        dct.setdefault(el, 0)
        dct[el] += 1

    print(dct)
