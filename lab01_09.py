list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1 = [1, 2, 3, 4, 5]

for i in list2[:]:  # iterate over a copy of list2
    if i in list1:
        list2.remove(i)  # remove from the original list2

print(list2)
