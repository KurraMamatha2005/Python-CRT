n=int(input("enter the value of n:"))
temp = n
digitcount=0
while(n!=0):
  n=n//10
  digitcount+=1#digitcount = digitcount+1
print(f"{temp} has {digitcount} digits ")
