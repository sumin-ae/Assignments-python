names=['Sumin', "Sumit", 'Suprima', 'Sumit', 'Sumin']

# name_count = {} #empty dictionary initialize gareako
# count=0
# for i in names: #names bhanne list ma itterate garxa 
#     if i in name_count:
#         count +=1  # Increase count if name already seen
#     else:
#         name_count[i]==1   # Add name to dictionary if new
    

# print(name_count)

d = {}
for name in names:
    if name not in d.keys():
        d[name] = names.count(name)
print(d)

