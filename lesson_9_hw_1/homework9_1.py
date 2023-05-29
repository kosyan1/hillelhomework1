def difference(*args):
    if not args:
        return 0
    else:
        min_val = min(args)
        max_val = max(args)
        return max_val - min_val

while True:
    user_input = input("Введіть числа, розділені пробілом: ")

    numbers = []

    input_numbers = user_input.split()

    for num in input_numbers:
        numbers.append(float(num))

    result = difference(*numbers)

    if result.is_integer():
        result = int(result)

    print(result)
