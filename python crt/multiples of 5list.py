size=int(input("enter the size of the list"))
list=[]
newlist=[]
#reading list as input
for i in range(size):
   Temp=int(input(f"enter elements in list at {i} position:"))
   list.append(Temp)
print(list)
for i in list:
   if i%5==0:
      newlist.append(i)
print(newlist)
