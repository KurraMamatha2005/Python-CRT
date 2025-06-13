n = int(input())
if(n>0):
  print(f"{n} is positive")
elif(n<0):
   print(f"{n} is negative")
else:
    print(f"{n} is 0")
#using terenary operator
Res="positive" if(n>0) else "negative"
print(f"{n}is{Res}")