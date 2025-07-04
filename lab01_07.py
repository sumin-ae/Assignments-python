

dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 100, 'd': 400}

merged_dict = {}

#dictionary lai key ma convert gareako so common key lai 
for key in set(dict1) | set(dict2): #union operator to make sure duitai dictionary ko key add up hos 
    if key in dict1 and key in dict2:
        
        merged_dict[key] = dict1[key] + dict2[key]
    elif key in dict1:
      
        merged_dict[key] = dict1[key]
    else:
       
        merged_dict[key] = dict2[key]

print(merged_dict)
