n=int(input("enter integer:"))
temp=n
sum = 0
rem=0
while n!=0:
    rem = n%10
    sum = sum+rem
    n=n//10
print(f"the sum of digits in {temp} is {sum}")