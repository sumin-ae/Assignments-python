# Create Account class with 2 attributes- balance and account no 
# create metjopds for debit, credit and printing hte balance 
class Account:
  def __init__(self,balance,account):
    self.balance=balance
    self.account=account
  #debit method
  def debit(self,amount):
    self.balance -=amount
    print("Rs", amount, "Was debited")
    print("The Final Balance is",self.balance)
  def credit(self,amount):
    self.balance +=amount
    print("Rs", amount, "Was credited")
    print("The Final Balance is",self.balance)
  def __str__(self):
    return f"Your account number is {self.account} and Current balance is {self.balance}"

acc1=Account(47050,121324)
print(acc1)
acc1.debit(1900)
acc1.credit(2000)


