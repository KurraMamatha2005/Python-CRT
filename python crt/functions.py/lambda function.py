g="good morning"
def display():
    g="afernoon"
    print(g)
display()
#here if we can local variable dominance over global variable
#to acess global variable
print(g)

#lambda function 
res=lambda a:print(a)
res("hello")

re= lambda b,c:print(b+c)
re(1,2)

pn= lambda d:print("+ve") if (d>0) else print("-ve")
#here we used ternerary operator value_conditionistrue if (condition) else value_if_false
pn(3)
#for multiple conditions
n= lambda e:print("+ve") if (e>0) else print("-ve") if (e<0) else print("0") 
n(0)
 
std= lambda n:print("good students") if (n=="bioinformatics") else print("badstudents")
std("bioinformatics")




