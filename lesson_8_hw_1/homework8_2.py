def add_one(digits):
    additive = 1
    i = len(digits) - 1

    while i >= 0:
        sum = digits[i] + additive
        digits[i] = sum % 10
        additive = sum // 10
        i -= 1

    if additive:
        digits.insert(0, additive)
    return digits

while True:
    vvod = input("Введіть список цифр, розділених пробілом: ")

    digits = []
    split_input = vvod.split()

    for digit in split_input:
        digits.append(int(digit))
    result = add_one(digits)

    print(f"Результат: {result}")
