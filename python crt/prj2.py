#programm to 
#take a list of toy names
#remove duplicates
#sort and display the final toy to pack
Toy_List=['tom','barbie','lego','cars','cars','puzzels','barbie']
print(Toy_List)
New_List=[]
for i in Toy_List:
    if i not in New_List:
       New_List.append(i) 
print(New_List)



# add 10 songs to playlist 
#print in normal and reverse order
playlist=[]
song=int(input("enter number of songs"))
for i in range(song):
    songs=input(f"enter song{i+1} :")
    playlist.append(songs)
print(playlist)
playlist.reverse()
print(playlist)


#input a list of numbers
#create two new list : one for even numbers,one for odd numbers
#dispay both list
num=[2,3,4,5,6,7,8,9]
print(num)
even_list=[]
odd_list=[]
for i in num:
  if i%2==0:
        even_list.append(i)
  else:
        odd_list.append(i)
#input a list of numbers
#create two new list : one for even numbers,one for odd numbers
#dispay both list
num=[2,3,4,5,6,7,8,9]
print(num)
even_list=[]
odd_list=[]
for i in num:
  if i%2==0:
        even_list.append(i)
  else:
        odd_list.append(i)
print(odd_list)
print(even_list)

#store 10 students name
#swap positions of any 10 students
#print the new seating elements
size=int(input("enter the number of students name"))
students=[]
for i in range(size):
    temp=input(f"enter the name of student {i+1} :")
    students.append(temp)
    print(students)
for i in students:
   k=students[4]
   students[4]=students[3]
   students[3]=k
print(students)

                




