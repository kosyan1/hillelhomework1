def is_even(n: int) -> bool:
    if n & 1 == 0:
        return True
    else:
        return False

while True:
    n = input("Введіть число: ")
    num = int(eval(n))

    result = is_even(num)

    print(result)
