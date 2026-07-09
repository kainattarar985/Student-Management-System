from student import Student

student1 = Student("Abdullah", 21, "S001", "Computer Science", "A", "Male", 2, "A", "abdullah@example.com", "123-456-7890", "123 Main St", 3.8)
student1.display()

student2 = Student("Haider", 22, "S002", "Mathematics", "B", "Male", 3, "B", "haider@example.com", "098-765-4321", "456 Oak Ave", 3.5)
student2.display()

student3 = Student("Mariam", 19, "S003", "Physics", "A", "Female", 1, "C", "mariam@example.com", "555-555-5555", "789 Pine Rd", 3.9)
student3.display()

students=[]

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        print("Add student selected")

    elif choice == '2':
         print("Display students selected")

    elif choice == '3':
        print("Exiting the program.")

    else:
        print("Invalid choice. Please try again.")
