class BankAccount:
  def __init__(self,account_number,balance):
    self.__account_number=account_number #private bhayo aaba
    self.__balance=balance
  
  def deposit(self,amount):
    if amount>0:
      self.__balance+=amount
      print(f"Deposited {amount}. New balance: {self.__balance}")
    else:
      print("Deposit amount must be greater than zero")
    
  def withdraw(self,amount):
    if amount<=self.__balance and amount>0:
      self.__balance-=amount
      print(f"Withdrew {amount}. Remaining Balance: {self.__balance}.")
    elif amount<=0:
      print("the withdrawal amount must be positive")
    else:
      print("insufficient Balance")

  def getdetails(self):
    print(f"Account NUmber: {self.__account_number}")
    print(f"Balance: {self.__balance}")


acc1 = BankAccount("123456789", 1000)


acc1.getdetails()
acc1.deposit(500)
acc1.withdraw(200)
acc1.withdraw(2000)   # should show insufficient balance
acc1.getdetails()
