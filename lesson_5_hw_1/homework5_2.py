while True:
    vvod = int(input("Введіть ціле додатнє число, цифри якого потрібно перемножити, поки не вийде\
число меньше або дорівнює 9: "))

    if vvod <= 0:
        print("Введіть ціле додатнє число!")
    else:
        while vvod > 9:
            new_vvod = 1
            for digit in str(vvod):
                new_vvod *= int(digit)
            vvod = new_vvod

        print(vvod)
