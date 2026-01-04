# these are of two types: class attributes and instance attributes
#class attributes are shared by all instances of the class
#instance attributes are unique to each instance
class Student:
    college_name = "ABC College"  #class attribute
    def __init__(self, name, cgpa):  #instance attributes
        self.name = name
        self.cgpa = cgpa

stu1 = Student("Rahul", 8.5)
stu2 = Student("Anjali", 9.0)
print("Student 1 Name:", stu1.name)
print("Student 1 CGPA:", stu1.cgpa)
print(stu1.college_name)  #accessing class attribute