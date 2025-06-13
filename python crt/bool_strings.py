print(bool(10))
print(True+True)
print(True+False)
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(range(0)))
print(bool(set()))


#strings
str1='good morning'
print(str1)
print(type(str1))
#double quotes
str2="we are in python"
print(str2)
print(type(str2))
#using triple quotes
str3='''i love python'''
print(str3)
print(type(str3))
#double triple quotes
str4="""we learning strings"""
print(str4)
print(type(str4))
#single quotes highlighting dbl quotes
str5='i want to learn"java" programming'
print(str5)
print(type(str5))

# identity operators
a=20
b='20'
print(a is b)# returns false becoz adress of a and bare different due to diff datatype if a and b are like 20 and 20 their adress is same and idenity oprstor returns trued

#acessing string without index
s="python"
print(f"len of{s} is {len(s)}")
for i in s:
    print(i,end="")

#aceesing with index
for i in range(len(s)):
    print(s[i],end=" ")#end used such that to print txt in one line we give space in end then it is replicated in output

#str7 = "students"
#str7[4]="i"
#for c in str7:
   # print(c)      we get error becoz we try to modify the strings
str8="python programming"
print(str8[2:7])
print(str8[0])
print(str8[7:11])
print(str8[10:14])
print(str8[7:10])
print(str8[2:6])
print(str8[::-1])
print(str8[5::-1])

#repetion operation on str
str7="students"
print(str7*3)
print(str7[0:4]*3)

print(10,'20')
#when data types are same + willwork (conacatination) when data types are differnent we use , to concatinate
a='hello'
b='world'
c=a+b
print(c)
# trimming the spaces
Input=input("enter the user entered string:")
print(f"the sting is {Input}")
print(Input.strip())
print(Input.split())
# conversion of list to string
In=input("enter str")
print(f"user enterd str:{In}")
str_List=In.split()
res=''.join(str_List)
print(f"string with out spaces {res}:") 



