class Mobile:
    def __init__(self):
        print("object is created")
    @classmethod  #it is a decorator used to represent class method
    def Display(Class):
        print("i am a class method")
        print("i will work irrespective of objective creation")
Mobile.Display()
M1=Mobile()
M1.Display()

"""class Mobile:
    def __init__(self):
        print("object is created")
    @staticmethod 
    def Display():
        print("i am a class method")
        print("i will work irrespective of objective creation")
Mobile.Display()
M1=Mobile()
M1.Display()"""

#write a python program to create a bookclass declare the states as 
# book Name
#authorname
#publishername
#categoryofbook
#i)create 5 objects and intialize the values using constructor where out of five
#   create 1st object using one parameterized constructor
#   create 2nd object using two parameterized constructor
#   create 3rd object using third parameterized constructor
#   create 4th object using four parameterized constructor
#   create 5th object using five parameterized constructor
#ii)access the value accessor methods
#iii)updatethevalues using mutator method for the name book


"""write a python programm to cretae a shape class & declare the propert as 
length
breadth
height
i) calculate the are of square using instance methods
ii) check whether the slides of square's are equal or not using instance method
iii)calcualte the perimeter of square using instance methods
iv)find the diagnols of square using instance methods
v) find the side length of square using instance methods"""


class Book:
    def __init__(self,book_name,author_name,publisher_name,category):
        self.Book=book_name
        self.Author=author_name
        self.Publisher=publisher_name
        self.Category=category
    def set_details(self):
        self.Book="medicine"
        self.Author="mamu"
        self.Publisher="mamatha"
        self.Category="biology"
    def get_details(self):
        print(f"thebook name is:{self.Book}")
        print(f"the author of book is :{self.Author}")
        print(f"the publisher of book is :{self.Publisher}")
        print(f"the category of book:{self.Category}")
B1=Book("botany","frog","lion","plant")
B1.get_details()
B1.set_details()
B1.get_details()


