import random

while True:
    def common_element(number_1, number_2):
        list1 = []
        count = 0
        while count < number_1:
            random_number = random.randint(3, 100)
            if random_number % 3 == 0:
                list1.append(random_number)
                count += 1

        list2 = []
        count = 0
        while count < number_2:
            random_number = random.randint(5, 100)
            if random_number % 5 == 0:
                list2.append(random_number)
                count += 1

        print(list1)
        print(list2)

        set1 = set(list1)
        set2 = set(list2)

        intersection = set1 & set2

        return intersection


    number_1 = int(input("Введіть кількість елементів першого списка: "))
    number_2 = int(input("Введіть кількість елементів другого списка: "))

    result = common_element(number_1, number_2)

    print(result)
