"""
Part_4.py.

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
    schools = []

    for i in range(2):  # Loop to create 2 school objects
        print(f"\nSchool {i+1} Information")
        name, students, classrooms = get_school_info()
        schools.append(School(name, students, classrooms))

    print("\nSchool Data:")  
    for school in schools:
        school.show_info()

    # Extension: Find and display the school with the lowest class size
    smallest_school = min(schools, key=lambda s: s.avg_students_per_classroom())
    print("\nSchool with the lowest class size:")
    smallest_school.show_info()

if __name__ == "__main__":
    main()
