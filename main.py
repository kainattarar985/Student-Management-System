from student import Student

def add_student(students):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    student_id = input("Enter student ID: ")
    course = input("Enter course: ")
    grade = input("Enter grade: ")
    gender = input("Enter gender: ")
    year = int(input("Enter year: "))
    section = input("Enter section: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    address = input("Enter address: ")
    cgpa = float(input("Enter CGPA: "))

    new_student = Student(name, age, student_id, course, grade, gender, year, section, email, phone, address, cgpa)
    students.append(new_student)
    print(f"\nStudent {name} added successfully!\n")

def display_students(students):
    if not students:
        print("\nNo students to display.\n")
        return
    for student in students:
        student.display()

student1 = Student("Abdullah", 21, "S001", "Computer Science", "A", "Male", 2, "A", "abdullah@example.com", "123-456-7890", "123 Main St", 3.8)
student2 = Student("Haider", 22, "S002", "Mathematics", "B", "Male", 3, "B", "haider@example.com", "098-765-4321", "456 Oak Ave", 3.5)
student3 = Student("Mariam", 19, "S003", "Physics", "A", "Female", 1, "C", "mariam@example.com", "555-555-5555", "789 Pine Rd", 3.9)

students = [student1, student2, student3]

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        add_student(students)
    elif choice == '2':
        display_students(students)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")