def roman_to_integer(s):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    past_value = 0

    for symbol in reversed(s):
        actual_value = roman_values[symbol]
        if actual_value >= past_value:
            result += actual_value
        else:
            result -= actual_value
        past_value = actual_value
    return result

while True:
    s = input("Введіть римське число: ")

    print(f"Число {s} дорівнює: {roman_to_integer(s)}")
