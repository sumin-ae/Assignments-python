# Write a program to find the largest and smallest number in a list entered by
# the user.
numbers = []
print("Enter the 10 list elements")

for i in range(10): 
  numbers[i]=int(input("Enter the number of the list"))
largest = max(numbers)
smallest = min(numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)