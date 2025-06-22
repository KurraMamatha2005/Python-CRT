#constructor without parameter
class Mobile:
    def __init__(self):
        print("Mobile constructor Called")#constructor is a method which automatically invoked when the object is created
realme=Mobile()

###############################
class Moble:
    def __init__(self):
        self.model="realme x"
    def show_model(self):
        print("Model:",self.model)

realme=Moble()
realme.show_model()

class Student:
    def __init__(self):#every time self key word is converted into object reference,,self holds adress of object
        pass
    def Display(self):
        print(self)
S1=Student()
S1.Display()
S2=Student()
S2.Display()# self holds adress of object reference of the keyword like here holds s2 adress


#object methods 2 types
#1.acessor method ,  2. Mutator method

#mutator method
#getter method only works for that particular method
class Employee():
   def __init__(self,empname,empid,designation,salary,deptname):
      print("object is created")
      self.Empname=empname
      self.Empid=empid
      self.Designation=designation
      self.Salary=salary
      self.Deptname=deptname
   def Get_Details(self):
            print( self.Empname)
            print( self.Empid)
            print(self.Designation)
            print(self.Salary)
            print(self.Deptname) 
E1=Employee("scott","Emp101","data analyst","2500","deployment teM")
E1.Get_Details()


#using mutator method
class Mobile:
    def __init__(self,P,C,B):
        self.Price=P
        self.Color=C
        self.Brand=B
        print("object is created")
        #mutator
    def set_Color(self):
        self.Color='blue'
        #accessor
    def Get_Details(self):
        print(f"price:{self.Price}")
        print(f"Price{self.Color}")
        print(f"Brand{self.Brand}")
M1=Mobile(1200,'black','samsung')
M1.Get_Details()
M1.set_Color()
M1.Get_Details()

class Product:
    def __init__(self,name,id,price,gst,manufacture_date,expired_date):
        self.Name=name
        self.Id=id
        self.Price=price
        self.Gst=gst
        self.Manufactue_date=manufacture_date
        self.Expiry_date=expired_date
        print("product is done")
    def set_modify(self):
        self.Name="freedom"
        self.Id=234
        self.Price=300
        self.Gst=1000
        self.Manufactue_date=30
        self.Expiry_date=44
    def Get_product(self):
        print(f"the name is:{self.Name}")
        print(f"the id of product is:{self.Id}")
        print(f"the price of product:{self.Price}")
        print(f"the gst on product is:{self.Gst}")
        print(f"the manufacturadate :{self.Manufactue_date}")
        print(f"the expiry date is :{self.Expiry_date}")
P1=Product("dermaco","225","450","444","28","34")
P2=Product("selen","1590","220","3456","34","458")
P3=Product("kaybeauty","katreena","24069","432","24","56")
P4=Product("greta","34","42","35463","83","239")
P1.Get_product()
P1.set_modify()
P1.Get_product()
P2.Get_product()
P2.set_modify()
P2.Get_product()
P3.Get_product()
P3.set_modify()
P3.Get_product()
P4.Get_product()
P4.set_modify()
P4.Get_product()

#with out using constructor
class Students():
    def set_details(self,name,id,branch,percentage,age,year_paseed,certificates):
        self.Name=name
        self.Id=id
        self.Branch=branch
        self.Percentage=percentage
        self.Age=age
        self.Year_pased=year_paseed
        self.Certificates=certificates
    def set_modify_details(self):
        self.Name="mamu"
        self.Id="221fa14007"
        self.Branch="bi"
        self.Percentage=99
        self.Age=19
        self.Year_pased=2026
        self.Certificates=3
    def get_details(self):
        print(f"name of std:{self.Name}")
        print(f"id of std:{  self.Id}")
        print(f"branch of st:{ self.Branch}")
        print(f"percentage of std:{self.Percentage}")
        print(f"age of std is :{self.Age}")
        print(f"year of passed out is:{self.Year_pased}")
        print(f"certificates of std:{self.Certificates}")
S1=Students()
S1.set_details("keer", "221FA14032", "btech", 100, 22, 2022, 44)
S1.get_details()
S1.set_modify_details()
S1.get_details()
print("''''''''''''''''''''''''''''''''''''''''")
S2=Students()
S2.set_details("swarna", "221FA14036", "bca", 10, 25, 2032, 34)
S2.get_details()
S2.set_modify_details()
S2.get_details()

class Rectangle:4
    def __init__(self,length,breadth):
        print("rectangle created")
        self.Length=length
        self.Breadth=breadth
    def get_var(self):
        print(f"enter the length:{self.Length}")
        print(f"enter the breadth:{self.Breadth}")
    def set_var(self):
        self.Length=10
        self.Breadth=11
R1=Rectangle(12,4)
R1.get_var()
R1.set_var()
print("........................................")
R1.get_var()