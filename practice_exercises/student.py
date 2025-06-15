class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def student_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


student1 = Student("Marisana", 31)

student1.student_info()