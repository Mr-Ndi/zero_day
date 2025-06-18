class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.__grades = {}

    def add_grade(self, subject, score):
        self.__grades[subject] = score

    def get_average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades.values()) / len(self.__grades)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print("Grades:")
        for subject, score in self.__grades.items():
            print(f"  {subject}: {score}")
        print(f"Average: {self.get_average():.2f}")

    def get_grades(self):
        return self.__grades.copy()

