"""
functions_lists.py.

Created by: Arkin E
Date: 26.02.2024
"""

class Student:
    def __init__(self, name: str, id: int, grades: list[int]):
        self.name = name
        self.student_id = student_id
        self.grades = grades


    def calculate_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


    def add_grade(self, grade: int) -> None:
        self.grades.append(grade)


# Example usage
student1 = Student("Alice", 1001, [90, 85, 92, 88])
student2 = Student("Bob", 1002, [78, 95, 89, 91])


# Display initial average grades
print(f"{student1.name}'s average grade: {student1.calculate_average()}")
print(f"{student2.name}'s average grade: {student2.calculate_average()}")


# Add new grades
student1.add_grade(94)
student2.add_grade(87)


# Display updated average grades
print(f"\nAfter adding grades:")
print(f"{student1.name}'s average grade: {student1.calculate_average()}")
print(f"{student2.name}'s average grade: {student2.calculate_average()}")
