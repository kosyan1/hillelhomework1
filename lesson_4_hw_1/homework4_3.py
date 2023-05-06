while True:
    age = int(input("Age: "))

    if 0 < age < 2:
        print("baby")
    elif 2 <= age < 4:
        print("kid")
    elif 4 <= age < 13:
        print("child")
    elif 13 <= age < 20:
        print("teenager")
    elif 20 <= age < 65:
        print("grown-up")
    elif 65 <= age:
        print("senior")
    else:
        print("Введіть ціле додатнє число!")
