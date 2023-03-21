class Student:
    roll = ""
    gpa = ""

    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll = {self.roll}, GPA = {self.gpa}")

rohim = Student(101,3.70)
rohim.display()

korim = Student(102,3.50)
korim.display()