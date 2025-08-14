# Write a Python function named greet_user that takes a user's name and prints:
#  Hello, <name>! Welcome to Python. Call the function with a sample name.

def greet_user(name):
  print(f'Hello, {name}! Welcome to Python.')

name=input("Enter Your Name")
greet_user(name)