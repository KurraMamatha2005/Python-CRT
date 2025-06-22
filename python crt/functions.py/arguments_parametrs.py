#nested function
def eat():
    def washhands():
     print("wash hands")
    def servefood():
     print("eat")
    print("enjoy meal")
    washhands()
    servefood()#while declaring nested function function inside function we hsve to call function to get the output
eat()

def hello():
  print("hello")
print(hello())
# the output for above code
#hello
#None  hello() runs:
#Prints hello
#Returns None
#Then, print() prints the return value of hello(), which is None.

#while function decleration or function definition the value given inside paranthesis is parameter
#while calling function the variable gven inside parenthesis called argument
#parameters are formal arguments
#function call arguments are actuall arguments
def add(x,y):#formal argumnts
     c=x+y
     print(c)
add(10,20)#actuall arguments

#positional arguments
def pw (s,d):
   z=s**d
   print(z)
pw (5,2)
#key word argument
def show(name, age):
   print(name, age)
show(name="mamu", age=19)
#default arguments
def show (name, age=27):
   print(name, age)
show(name="raam", age=62)# here we change the during function decleration we gave 27 now 62 by default it writes 62
#variable length arguments
#Use *args when you don’t know how many positional arguments will be passed to the function.
def disp(*x):
   x=x[0]+x[1]+x[2]+x[3]
   print(x)
disp(10,20,30,40)
#keyword variable length arguments
#Use **kwargs when you don’t know how many keyword arguments (i.e., key=value) will be passed.
def add (**n):
   z= n['a']+n['b']+n['c']
   print(z)
add(a=10, b=2, c=5)
   

