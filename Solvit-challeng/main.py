from student import Student
from manager import StudentManager

if __name__ == "__main__":
    manager = StudentManager()

    s1 = Student("Alice", "A001")
    s1.add_grade("Math", 85)
    s1.add_grade("Science", 90)

    s2 = Student("Bob", "A002")
    s2.add_grade("Math", 95)
    s2.add_grade("Science", 88)

    manager.add_student(s1)
    manager.add_student(s2)

    print("\nAll Students:")
    manager.list_students()

    top_student = manager.get_top_student()
    if top_student:
        print("\nTop Student:")
        top_student.display_info()

