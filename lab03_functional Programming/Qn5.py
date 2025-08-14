# Write a function student_profile(**kwargs) that prints the key-value pairs passed (e.g., name, age,
# grade). Call it with at least three named arguments.
def student_profile(**kwargs):
  for key, value in kwargs.items():
    print(f'{key}: {value}')

student_profile(name="Sumin Giri", age=19, grade="A")