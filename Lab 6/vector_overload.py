#operator overriding to add two vectors: 
class Vectors:
  def __init__(self,i,j,k):
    self.i=i
    self.j=j
    self.k=k
  def __add__(self,other):
    return Vectors(self.i+other.i,self.j + other.j, self.k + other.k)
  def __str__(self):
    return f'{self.i}i + {self.j}j + {self.k}k'
  

v1 = Vectors(1, 2, 3)
v2 = Vectors(4, 5, 6)

v3 = v1 + v2   # Uses __add__ or you can write v1.__add__(v2)

print(v1)  # 1i + 2j + 3k
print(v2)  # 4i + 5j + 6k
print(v3)  # 5i + 7j + 9k
