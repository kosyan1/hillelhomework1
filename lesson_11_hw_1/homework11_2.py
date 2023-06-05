from typing import List

def generate_cube_numbers(limit: int) -> List[int]:
    num = 2
    while True:
        cube = num ** 3
        if cube <= limit:
            yield cube
            num += 1
        else:
            return

while True:
    limit = int(input("Введіть верхню межу чисел: "))

    cube_nums = list(generate_cube_numbers(limit))

    print(cube_nums)
