from student import Student
from group import Group

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)

print(gr)
print(gr.find_student('Jobs'))   # Виведе інформацію про Стіва Джобса
print()
print(gr.find_student('Jobs2'))  # Виведе None, оскільки студента з таким прізвищем немає в групі
print()
gr.delete_student('Taylor')

print(gr)  # Буде виведено інформацію тільки про Стіва Джобса, оскільки Ліза Тейлор була видалена
