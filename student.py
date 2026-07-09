class Student:
    def __init__(self, name, age, student_id, course, grade,gender,year,section,email,phone,address,cgpa):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.course = course
        self.grade = grade
        self.gender = gender
        self.year = year
        self.section = section
        self.email = email
        self.phone = phone
        self.address = address
        self.cgpa = cgpa

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")
        print(f"Grade: {self.grade}")
        print(f"Gender: {self.gender}")
        print(f"Year: {self.year}")
        print(f"Section: {self.section}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
        print(f"CGPA: {self.cgpa}")
        print("-"*30)
        
    