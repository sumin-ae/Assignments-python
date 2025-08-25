# Create a base class Animal with a method speak() that prints "Animal makes
# a sound". Derive a class Dog from Animal and override the speak() method
# to print "Dog barks". Instantiate the Dog class and call its speak() method.

class Animal: 
  def speak():
    print("Animal Makes a Sound")
class Dog:
  def __init__(self,name):
    self.name=name
  def speak(self):
    print(f'{self.name} Barks')

Dog1=Dog("Dharampal")
Animal.speak()
Dog1.speak()
