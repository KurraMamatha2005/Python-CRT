set={10,20,30,40,50,60,70}
print(set)
#in set there is no order no index position
print(type(set))
print(10 in set)
set.add(35)
print(set)
set.remove(20)
print(set)
#update add multiple elements to a set
a={'e','r'}
set.update(a)
print(set)
set.discard(45)
#discard and remove both methods are same but remove gives an error were dicard not give error if the element  not present in the set
set.pop()
print(set)
# clear removes all the elements from the set
set.clear()
print(set)
#union returns a set combining all unique element from both set
set1={1,2,3}
set2={3,4,5}
print(set1|set2)
#intersection returns common elements
print(set1&set2)
#difference returns items present only in first set 
#symmetric difference returns a set containing items that are in either set but not both
print(set1-set2)#difference
print(set1^set2)#symmetric difference
set1.intersection(set2)
print(set1)
set1.union(set2)
print(set1)
set1.difference(set2)
print(set1)
#subset and superset
set_a={4,6,8}
set_b={2,4,6,8}
print(set_a.issubset(set_b))
print(set_b.issubset(set_a))
print(set_a.issuperset(set_b))
print(set_b.issuperset(set_a))

#in string replace t eith
string=input("enter a sequence")
for i in string:
 string.replace(T,U)
 print(string)
