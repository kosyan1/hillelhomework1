while True:
    a = input("Введіть перше число, або 'quit' для виходу: ")
    if a == 'quit':
        break
    operation = input("Введіть математичну операцію, або 'quit' для виходу: ")
    if operation == 'quit':
        break
    b = input("Введіть друге число, або 'quit' для виходу: ")
    if b == 'quit':
        break

    a = float(a)
    b = float(b)

    i = 0

    if operation == '+':
        i = a + b
    elif operation == '-':
        i = a - b
    elif operation == '*':
        i = a * b
        if i == -0.0:
            print('Результат: 0.0')
            continue
    elif operation == '/':
        if b == 0:
            print('На нуль ділити не можна!')
            continue
        else:
            i = a / b
            if i == -0.0:
                print('Результат: 0.0')
                continue
    else:
        print('Даний калькулятор такого не вміє')
        continue
    print(f"Результат: {i:.3f}")
