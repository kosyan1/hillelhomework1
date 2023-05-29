def some_gen(begin, n, func):
    """
    begin: перший член послідовності
    n: кількість елементів у послідовності
    func: функція, яка формує значення для послідовності
    """
    i = 0
    while i < n:
        yield begin
        begin = func(begin)
        i += 1

def pow(x):
     return x ** 2

while True:
    begin = int(input("Введіть початковий член послідовності: "))
    n = int(input("Введіть кількість елементів у послідовності: "))

    result = list(some_gen(begin, n, pow))

    print(result)
