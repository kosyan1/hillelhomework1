while True:
    a = input("Введіть список значень розділених знаком ',' без пробілів: ")
    a = a.split(',')

    middle = len(a) // 2

    if len(a) % 2 != 0:
        middle += 1

    first_half = a[:middle]
    second_half = a[middle:]

    if first_half == ['']:
        first_half = []
    result = [first_half, second_half]
    print(result)
