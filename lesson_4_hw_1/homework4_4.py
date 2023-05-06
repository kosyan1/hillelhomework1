while True:
    a = int(input('Введіть висоту рівнобічного трикутника: '))

    i = 0
    while i < a:
        spaces = ' ' * (a - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
        i += 1
