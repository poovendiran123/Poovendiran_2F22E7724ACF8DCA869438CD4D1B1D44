#Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.
class Student:
    def _init_(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Create a list of 5 student objects for testing
students = [
    Student("gokul", "A123", 4.8),
    Student("Krishna", "B456", 3.5),
    Student("Ilavarasan", "C789", 3.9),
    Student("gopal", "D234", 3.2),
    Student("Lakshmikant", "J234", 3.3)
]

# Sort the list of students by CGPA
sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")