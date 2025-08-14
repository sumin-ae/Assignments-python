#  Write a function book_info(title, author, year) that prints book details.Call the function using
# keyword arguments in different orders.

def book_info(title,author,year):
  print(f'The title of the book is {title}')
  print(f'The author of the book is {author}')
  print(f'The year of pulblishing of the book is {year}')
  
print(book_info(year='2025',author='Sumin Giri', title="Learn Python With Sumin"))