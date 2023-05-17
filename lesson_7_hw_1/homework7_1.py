while True:
    def say_hi(name, age):
        return f"Hi. My name is {name} and I`m {str(age)} years old"

    name = input("Введіть ім`я: ")
    age = int(input("Введіть вік: "))

    result = say_hi(name, age)

    print(result)
