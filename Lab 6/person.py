class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

class Employee(Person):
  def __init__(self, name, age,employee_id,salary):
    super().__init__(name, age)
    self.__employee_id=employee_id
    self.salary=salary
  def get_id(self):
    return self.__employee_id

  def display_employee(self):
    print(f'The Name of the Employee is {self.name}\n His/her age is{self.age}\n His employee id is{self.get_id()} \n and his salary is {self.salary}')


# Create an Employee object
emp1 = Employee("Sumin", 22, "E101", 50000)

# Display details
emp1.display_employee()
