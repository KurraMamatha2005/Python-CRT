sentence="we are learning python"
list=sentence.split()
print(list)

str=input("enter the string")
print(str[::-1])
print(str.lower())
print(str.upper())
print(str.swapcase())
print(str.count('a'))
str=str.lower()
print(str.replace('p','j'))

#programm to read list of characters and convert into word

n = int(input("Enter number of characters: "))

# Create an empty list
char_list = []

# Take input for each character
for i in range(n):
    ch = input("Enter character : ")
    char_list.append(ch)
print(char_list)
st="".join(char_list)
print(st)

#seperating email using split function
email="mamthakuraa@gmail.com"
list=email.split('@')
print(f"user name:{list[0]}")
org=list[1]
print(list)
list=org.split('.')
print(f"org name:{list[0]}")

s="python programming"
print(s.capitalize())
print(s.title())
print(s.casefold())
print(s.startswith('p'))
print(s.find('o'))


t=input("enter the string")
uppercase_aplha=0
lowercase_alpha=0
numeric=0
special_char=0
for ch in t:
    if ch.isupper():
        uppercase_alpha+=1
    elif ch.lower():
        lowercase_alpha+=1
    elif ch.isdigit():
        numeric+=1
    else:
        special_char+=1
print(f"count of upper case leters : {uppercase_alpha}")
print(f"the count of lowercase letters: {lowercase_alpha}")
print(f"the counrt of numeric values:{numeric}")
print(f"count of special character: {special_char}")

