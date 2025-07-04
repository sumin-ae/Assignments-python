''' 
Create a tuple of 10 integers. Write a program to display the maximum and
minimum numbers from the tuple. '''
import random
l=[]
for i in range(10):
    l.append(random.randint(1,101))
intgrp= tuple(l) #typecasting the list into tuple sicne the tuple doesnt support methods ssuch as append adn are immutable 
print(intgrp)
max1=max(intgrp)
max2=min(intgrp)
print(f'Max value: {max1} and min.value={max2}')