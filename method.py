class Student:
    roll = ""
    gpa = ""

    def set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll = {self.roll}, GPA = {self.gpa}")

rohim = Student()
rohim.set_value(101,3.70)
rohim.display()

korim = Student()
korim.set_value(102,3.50)
korim.display()