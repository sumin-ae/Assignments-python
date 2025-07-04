# Write a Python function that accepts a list and returns a new list with only
# the even numbers from the original list.
import random
l=[]
for i in range(10):
    l.append(random.randint(1,101))
newlist=[]
for i in range(10): 
    if (l[i] % 2==0): 
        newlist.append(l[i])
    
print(f"The even numbners in the list are: {newlist}")
