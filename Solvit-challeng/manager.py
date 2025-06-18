from student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if self.find_student_by_id(student.student_id) is not None:
            print(f"Student with ID {student.student_id} already exists.")
            return
        self.students.append(student)

    def list_students(self):
        for student in self.students:
            student.display_info()

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def get_top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda student: student.get_average())

