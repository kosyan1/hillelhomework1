import random

my_list = []

for i in range(random.randint(3, 10)):
    my_list.append(random.randint(0, 100))
new_list = [my_list[0], my_list[2], my_list[-2]]

print(f"{my_list} == {new_list}")
