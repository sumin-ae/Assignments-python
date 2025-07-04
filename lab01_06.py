import random
#generating a random two lists 
list1=[]
list2=[]
for i in range(10):
    list1.append(random.randint(1,101))

for i in range(10): 
    list2.append(random.randint(1,101))
#converting the list elements into set 

set1=set(list1)
set2=set(list2)
intersection= set1 & set2
print(f"The original list1 was {list1} and the 2nd list was {list2} ")
print(f'The intersection elements are: {intersection}')
