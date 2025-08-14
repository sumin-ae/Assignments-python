# Create a function sum_numbers(*args) that accepts any number of numeric arguments and returns
# their sum.Test it with 2, 3, and 5 numbers.

def sum_numbers(*args):
  sum=0
  for num in args:
    sum+=num
  print(f'The sum of the numbers is {sum}')

sum_numbers(15,24,124,124,133,2134)