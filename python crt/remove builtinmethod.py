num=[11,22,33,44,55,66,77,88,99]
print(num)
num.pop()
print(num)
num.pop(4)
print(num)
num.remove(77)
print(num)

#remove duplicates from the list without using predefined methods or functions
list=[12,24,67,98,98,74,65,65,74]
print(list)
fresh=[]
for i in list:
   if i not in fresh:
      fresh.append(i)
print(fresh)

   
