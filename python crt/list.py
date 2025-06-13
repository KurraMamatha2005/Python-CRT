n_list=[10,20,30,40,50,60,70,80,90]
print(n_list)
print("Acessing the list elements using forloop with out indexing")
for i in n_list:
    print(i)
print("Acessing the list elements using forloop with indexing")
#range(stop),range(start,stop,stepsize),rane(start,stop)
for i in range(len(n_list)):
    print(n_list[i])
print("Acessing the list elements using while loop with indexing")
i=0
while(i<len(n_list)):
    print(n_list[i])
    i+=1



#list input
size=int(input("enter size of list:"))
prog_lang=[]
#reading list as input
for i in range(size):
    Temp=input("enter a programming language:")
    prog_lang.append(Temp)
print("Elements of the list")
print(prog_lang)

#delete an element from a list
colors=['white','red','blue','black','green']
print(colors)
del colors[2]
print(colors)
del colors
print(colors)#here there should be error because we are calling deleted list


#repetion of list 
b=["a,b,s"]
re=b*3
print(re)
    

    




