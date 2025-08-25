class Book:
  def __init__(self,title,author):
    self.title=title
    self.author=author
  
  def __str__(self):
    return f"{self.title} by the author {self.author}"

book1=Book("Jujutsu Kaisen","Gege Akutami")
print(book1)