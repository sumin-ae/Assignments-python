# Given a list of numbers [1, 2, 3, 4, 5], use map() and a lambda function to return a new list with
# each number doubled.

numbers = [x for x in range(1,6)]
print(f'The original list of numbers were {numbers}')

new_numbers=list(map(lambda x:x*2,numbers))
print(f'The doubled list of numbers were {new_numbers}')
