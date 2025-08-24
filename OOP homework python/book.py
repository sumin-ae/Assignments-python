class Book: 
  def __init__(self,title,author,price):
    self.title=title
    self.author=author
    self.price=price

  def display_info(self):
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")
    print(f"Price: Rs.{self.price}")
  
  def update_price(self,newprice):
    self.price=newprice
    print(f"Price is updated to Rs.{self.price}")
  
#example usage 
book1=Book("The Alchemist", "Paulo coelho", 500)
book1.display_info()
book1.update_price(600)
book1.display_info()

