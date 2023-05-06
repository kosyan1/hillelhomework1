while True:
    a = input("Введіть список значень розділених знаком ',' без пробілів: ")
    a = a.split(',')

    if len(a) == 0:
        print("[[], []]")
    else:
        middle = len(a) // 2
        if len(a) % 2 != 0:
            middle += 1

        first_half = a[:middle]
        second_half = a[middle:]

        if first_half == ['']:
            first_half = []
        b = [first_half, second_half]
        print(b)
