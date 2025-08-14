# Write a lambda function to compute the square of a number.Use it to compute the square of 5 and
# # 12.

square= lambda x: x**2
numbers=[5,12]
squared_numbers=list(map(square,numbers))
print(squared_numbers)
