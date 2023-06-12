from student import Student

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
