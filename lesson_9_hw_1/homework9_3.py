def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

while True:
    n = int(input("Введіть число: "))

    result = factorial(n)

    print(f"Факторіал числа {n} дорівнює {result}")
