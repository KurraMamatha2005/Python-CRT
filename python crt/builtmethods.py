cartoons=["tom,doremon,shinchan,oggy"]
print(cartoons)
print("After appending")
cartoons.append("shaktishali dragan bayataki raaa")
print(cartoons)
#append adds element at ending of list
cartoons.insert(0,'chotaBhem')
print(cartoons)
#insert add elements at specific position
cartoons.pop()
print(cartoons)
#pop removes last element
#pop with index position removes element at specific position
cartoons.pop(0)
print(cartoons)
#remove element only removes first occurence of elements

num=[11,22,33,44,55,66,77,88,99]
print(num)
num.reverse()
print(num)

#with out using reverse buit in method
#slicing
num=[11,22,33,44,55,66,77,88,99]
print(num[::-1])
print(num[0:])
print(num[1:4+1])
print(num[::1])

num=[11,22,33,44,55,66,77,88,99]
num.remove(11)
print(num)


# use of extend
prog_Lang = ['c','c++','java']
print(prog_Lang)
front_end=['html','css','java']
print(front_end)
prog_Lang.extend(front_end)
print()

#to find thenumber of occuenece use count method
print(prog_Lang.count('html'))



