# Given a list [10, 15, 20, 25, 30], use filter() and a lambda function to extract numbers divisible by
# 10.
list1=[10, 15, 20, 25, 30]
filtered_list=list(filter(lambda x:x%10==0,list1 ))
print(f'The original list was {list1}')
print(f"the filtered list is {filtered_list}")