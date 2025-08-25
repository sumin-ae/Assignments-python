class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_info(self):
        print(f"The name of the student is {self.name}\nHis/Her roll no is {self.roll_no}")

    def calculate_marks(self, marks):
        print("Marks of the student are:")
        for mark in marks:
            print(mark,end=' ')

s1 = Student("Sumin", "081bel086")
s1.display_info()
s1.calculate_marks([90, 85, 78])
