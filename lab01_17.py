# Write a program to generate the Fibonacci sequence up to n terms.

n = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

if n <= 0:
  print("Please enter a positive integer.")
elif n == 1:
  print("Fibonacci sequence up to 1 term:")
  print(a)
else:
  print(f"Fibonacci sequence up to {n} terms:")
  while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1