# Given a list of temperatures in Celsius [36.5, 37.0, 39.2, 35.6, 38.7],convert them to Fahrenheit
# using map(),Filter out those above 100°F using filter().
ctof = lambda c:round((9/5) * c + 32,2)
temp1=[36.5, 37.0, 39.2, 35.6, 38.7]

print(f"The original list of temperatures are {temp1}")

temp2=list(map(ctof,temp1))
print(f"The list of temperatures in fahrenheit are {temp2}")
filtered=lambda x:x>100

filtered_temp=list(filter(filtered,temp2))
print(f"The list of temperatures greater than 100°F are {filtered_temp}")
