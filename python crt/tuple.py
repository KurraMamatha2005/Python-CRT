#deleting a tuole 
#tup = (0, 1, 2, 3, 4)
#del tup
#print(tup)
#creating tuple with out parenthesis
#tuple packing
tuple=10,20,30,40,50
print(type(tuple))
# tuple unpacking
n1,n2,n3,n4,n5=tuple   # if we give more n's than given values we get error as not enough values to unpack
print(n1,type(n1))
print(n2,type(n2))

#concatination of tuple means storing the tupes in another tuple
a=("geks","jeks","sekd")
b=(1,2,3)
tupl=a+b
print(tupl)

#repetion of tuplr
b=(1,2,3)
re=b*3
print(re)

#one tuple inside another tuple is called as nested tuple
tp=(('a','b','c'),('A','B','C'),(1,2,3),(-1,-2,-3))
print(tp)
for i in tp:
    print(i,type(tp))

#built in functions are common for all the data types rather than methods
t=(10,25,5,15,17,30,35)
print(t)
print("maximum number:",max(t))
print("minimum number:",min(t))
print("sorted tuple:",sorted(t))
print("summation:",sum(t))
print("length of tuple:",len(t))

t=(10,25,5,15,17,30,35)
print(t)
print("maximum number:",max(t))
print("minimum number:",min(t))
print("sorted tuple:",sorted(t))
print("summation:",sum(t))
print("reversed tuple"[::-1])

p=('python','c','java','html','css','angularjs','mongodb')
print(p)
print("maximum number:",max(p))
print("minimum number:",min(p))
print("sorted tuple:",sorted(p))
print("length of tuple:",len(p))
print("reversed tuple :",p[::-1])

u=('ram','shyam','veni','sakshi')
print(u)
for i in u:
    if len(i)==5:
        print(i)

#mapping of list to tupple
n=int(input("enter the number of words you like to find:"))
List=['marker','bread','black','wrist','class']
TU=('pen','jam','board','watch','room')
i=1
while(i<=n):
    word=input("enter the word:")
    index=List.index(word)
    print(f"{word}-{TU[index]}")
    i+=1

