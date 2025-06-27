import random
majorlist=[]
for i in range(15): 
  majorlist.append(random.randint(0, 500))
print("Lottery Numbers:",majorlist) 

list1 = majorlist[:5]
list2 = majorlist[5:10]
list3 = majorlist[10:]

sum1 = sum(list1)
sum2 = sum(list2)
sum3 = sum(list3)
print("Select a list")
print(''' 
          1-> List1
          2-> list2
          3-> list3''')
user_input=int(input("Enter the list number that you want to choose "))

print("\nList 1:", list1, "=> Sum:", sum1)
print("List 2:", list2, "=> Sum:", sum2)
print("List 3:", list3, "=> Sum:", sum3)

if sum1 > sum2 and sum1 > sum3:
    winner = "List 1"
    winning_list=1
elif sum2 > sum1 and sum2 > sum3:
    winner = "List 2"
    winning_list=2
elif sum3 > sum1 and sum3 > sum2:
    winner = "List 3"
    winning_list=3
else:
    winner = "It's a tie!"

# Announce the winner
print("\n🎉 Congratulations! You picked List", user_input, "which WON the lottery!")

