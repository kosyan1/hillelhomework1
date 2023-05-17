lst = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dct = {}

for key, value in lst:
    if key in dct:
        dct[key].append(value)
    else:
        dct[key] = [value]

print(dct)
