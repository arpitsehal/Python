class Employee:
    start_time ="10 AM"
    end_time = "6 PM"

class Teacher(Employee):
    def __init__(self,subject):
        self.subject = subject


t1 = Teacher("Math")

print(t1.subject ,"Working Hours:", t1.start_time , "to" , t1.end_time)