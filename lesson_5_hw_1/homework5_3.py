while True:
    number = input("Введіть список цілих чисел через кому без пробілів: ")
    lis = number.split(',')

    integer_list = list(map(int, lis))

    zeros = []
    non_zeros = []
    for value in integer_list:
        if value == 0:
            zeros.append(value)
        else:
            non_zeros.append(value)

    result = non_zeros + zeros
    print(result)
