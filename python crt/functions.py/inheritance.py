class Vehicle:
    #the instation of creating an object : car is sub class of the super class vehicle
    def __init__(self):
        print("i m the vehicle class constructor")
    @staticmethod  #it is a decorator it specifies to compiler that this method belongs to class
    def start():
        print("Vehicle started")
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("i m the car class constructor")
    @staticmethod 
    def start():
        print("car started")
C1=Car()
C1.start()
#single level inheritance
#if you are calling using sub class it print sub class implementation vice versa for super class
#method overriding
class Father:
    def __init__(self):
        pass
    @staticmethod  #it is a decorator it specifies to compiler that this method belongs to class
    def Work():
        print("hardworking father")
class Son(Father):
    def __init__(self):
        super().__init__()
    @staticmethod 
    def Work():
        print("enjoying son")
Father.Work()
Son.Work()

#multilevel inheritance
class GrandFather:
    def __init__(self):
        pass
    #method overriding
    @staticmethod  
    def Properties():
        print("100 acres of land")
class Father(GrandFather):
    def __init__(self):
        super().__init__()
    @staticmethod 
    def Properties():
        print("50 acres of land")
class You(Father):
    def Properties():
        print("25 acres of land")
GrandFather.Properties()
Father.Properties()
You.Properties()

#heirarchial inheritance
class Graduation:
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("congrats you are gradute")
#first sub class
class CSE():
    def __init__(self):
        super().__init__()
    @staticmethod
    def Graduate():
        print("you are a cse graduate")
#second sub class
class Bioinformatics():
    def __init__(self):
       super().__init__() 
    @staticmethod
    def Graduate():
        print("you are a bioinformatics graduate")
#third subclass
class ECE():
    def __init__(self):
        super().__init__()
    @staticmethod
    def Graduate():
        print("you are ece graduate")
Graduation.Graduate()
CSE.Graduate()
Bioinformatics.Graduate()
ECE.Graduate()

#multiple level inheritence
class Father:
    def skills(self):
        print("Father: Gardening, Driving")


class Mother:
    def skills(self):
        print("Mother: Cooking, Painting")


class Child(Father, Mother):  # Multiple inheritance
    def skills(self):
        print("Child: ", end="")
        super().skills()  # Will call Father's method (because Father is first in inheritance order)


c = Child()
c.skills()






