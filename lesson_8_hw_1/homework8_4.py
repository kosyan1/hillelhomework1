def find_unique_value(nums):
    unique_nums = set(nums)
    for num in unique_nums:
        if nums.count(num) == 1:
            if float(num).is_integer():
                return int(num)
            else:
                return num

while True:
    vvod = input("Введіть список чисел, розділених пробілом: ")

    nums = []
    split_input = vvod.split()

    for num in split_input:
        converted_num = float(num)
        nums.append(converted_num)

    result = find_unique_value(nums)

    print(f"Унікальне число: {result}")
