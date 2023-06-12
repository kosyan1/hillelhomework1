class Human:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"Name: {self.first_name} {self.last_name}\nGender: {self.gender}\nAge: {self.age}"

class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f"Student:\n{super().__str__()}\nRecord Book: {self.record_book}"

class Group:
    def __init__(self, number: str) -> None:
        self.number = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        self.group.add(student)

    def delete_student(self, last_name: str) -> None:
        res = self.find_student(last_name)
        if res is not None:
            self.group.remove(res)

    def find_student(self, last_name: str) -> Student:
        found_student = None
        for student in self.group:
            if student.last_name == last_name:
                found_student = student
                break

        return found_student

    def __str__(self) -> str:
        all_students = ""
        for student in self.group:
            all_students += str(student) + "\n\n"

        return f'Number: {self.number}\n{all_students}'

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
