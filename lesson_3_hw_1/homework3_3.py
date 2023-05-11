name_data = input(str("Напишіть данні в форматі 'Taras Shevchenko*1814-03-09*1861-03-10': "))
parts = name_data.split('*')
name = parts[0]
cut_data1, cut_data2 = parts[1].split('-'), parts[2].split('-')
data = int(cut_data2[0]) - int(cut_data1[0])

print(f"Name: {name}")
print(f"Age: {data}")
