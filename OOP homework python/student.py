class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def showdetails(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


s1 = Student("Sumin Giri", [100, 99, 78])
s2 = Student("Shubheccha Nepal", [90, 80, 70])
s3 = Student("Dimple Neupane", [99, 80, 79])

s1.showdetails()
s2.showdetails()
s3.showdetails()
