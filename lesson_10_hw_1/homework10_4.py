def lchain(*iterables):
    result = []
    for element in iterables:
        result.extend(element)

    return result

input_data = ([1, 2, 3, 4], {'5': 5}, tuple('55'), (6, 7), range(8, 11))

output = lchain(*input_data)

print(f"Результат виконання: {output}")
