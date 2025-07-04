list1=[]
for i in range(15): 
    append=int(input("Enter the list element"))

list1.append(append)
print(f"The unupdated list is {list1}")

unique_list=set(list1)
print(f" The unique list without any repeatation are {unique_list}")
