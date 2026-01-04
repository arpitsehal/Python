#_init_ Method (Constructor)
#use to initialize the object's attributes
class Student:
    def __init__(self, name, cgpa):     #self refers to the current instance of the class
        self.name = name
        self.cgpa = cgpa
        print("This is a constructor method")

stu1 = Student("Rahul", 8.5)  #when an object is created, the constructor is called automatically

print("Student Name:", stu1.name)
print("Student CGPA:", stu1.cgpa)