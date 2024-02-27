"""
Part_3.py.

Created by: Arkin E
Date: 26.02.2024
"""

class School:
    def __init__(self, school_name, num_students, num_classrooms):
        self.school_name = school_name
        self.num_students = num_students
        self.num_classrooms = num_classrooms

    def avg_students_per_classroom(self):
        return self.num_students / self.num_classrooms

    def show_info(self):
        average = self.avg_students_per_classroom()
        print(f"{self.school_name} has {average:.2f} students per room.")

def get_school_info():
    school_name = input("Enter the name of the school: ")
    num_students = int(input("Enter the number of students: "))
    num_classrooms = int(input("Enter the number of classrooms: "))
    return school_name, num_students, num_classrooms

def main():
    print("School 1 Information")
    name1, students1, classrooms1 = get_school_info()
    school1 = School(name1, students1, classrooms1)
    school1.show_info()

    print("\nSchool 2 Information")
    name2, students2, classrooms2 = get_school_info()
    school2 = School(name2, students2, classrooms2)
    school2.show_info()

if __name__ == "__main__":
    main()
