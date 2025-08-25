
class Time: 
  def __init__(self,hours,minutes,seconds):
    self.hours=hours
    self.minutes=minutes
    self.seconds=seconds
  
  def __eq__(self,other):
    return (self.hours==other.hours and self.minutes==other.minutes and self.seconds==other.seconds)
  
  def __str__(self):
    return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
  


time1 = Time(10, 30, 45)
time2 = Time(10, 30, 45)
time3 = Time(11, 20, 15)


print(time1 == time2)  # True
print(time1 == time3)  # False

# Printing for verification
print(time1)  # 10:30:45
print(time3)  # 11:20:15