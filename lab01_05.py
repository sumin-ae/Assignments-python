d1={'a':10, 'b':20, 'c':30}
d2={ 'a':20, 'b':30, 'd':40,'e':100}
for k,v in d1.items(): 
  if k in d2.keys():
    d2[k]=d2[k]+v
  else: 
    d2[k]=v
