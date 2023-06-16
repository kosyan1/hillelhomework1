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

class GroupException(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__()
        self.message = message

    def get_exception_message(self) -> str:
        return self.message

class Group:
    def __init__(self, number: str) -> None:
        self.number = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        if len(self.group) >= 10:
            raise GroupException("Максимальна кількість в групі - 10 студентів!")
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
st3 = Student('Female', 26, 'Svitlana', 'Orlova', 'AN146')
st4 = Student('Female', 27, 'Anna', 'Kramarenko', 'AN141')
st5 = Student('Female', 28, 'Olga', 'Ignatenko', 'AN140')
st6 = Student('Male', 29, 'Oleg', 'Cherbu', 'AN144')
st7 = Student('Male', 28, 'Mykola', 'Rysovanyi', 'AN121')
st8 = Student('Female', 27, 'Mariya', 'Muha', 'AN122')
st9 = Student('Male', 26, 'Dmytro', 'Kucher', 'AN133')
st10 = Student('Male', 24, 'Alex', 'Ivanov', 'AN134')
st11 = Student('Female', 25, 'Lena', 'Golovach', 'AN144')

gr = Group('PD1')

try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)
except GroupException as e:
    print(f"Помилка: {e.message}")

print(gr)
