class students():
    def __init__(self):
      print("i am a constructer and i will be automatically evovked")
S1=students()
S2=students()

class employee():
    def __init__(self):
      print("employee class constructer has been created")
S1=employee()
S2=employee()


class mobile():
   def __init__(self):
      print("samsung")
m1=mobile()
print(id(m1))
print(type(m1))
m2=mobile()
print(id(m2))
print(type(m2))
m3=mobile()
print(id(m3))
print(type(m3))
m4=mobile()
print(id(m4))
print(type(m4))
m5=mobile()
print(id(m5))
print(type(m5))

#constructor will create an object
class Employee():
   def __init__(self,empname,empid,designation,salary,deptname):
      print("object is created")
      self.Empname=empname
      self.Empid=empid
      self.Designation=designation
      self.Salary=salary
      self.Deptname=deptname
E1=Employee("scott","Emp101","data analyst","2500","deployment teM")
print(f"employee name:{E1.Empname}")
print(f"employee id:{E1.Empid}")
print(f"employee designation:{E1.Designation}")
print(f"employee salary:{E1.Salary}")
print(f"employee deptname:{E1.Deptname}")
def Display_Details(self):
   print(f"employee name:{self.Empname}")
   print(f"employee id:{self.Empid}")
   print(f"employee designation:{self.Designation}")
   print(f"employee salary:{self.Salary}")
   print(f"employee deptname:{self.Deptname}")
E1=Employee("scott","Emp101","data analyst","2500","deployment teM")
Display_Details(E1)

class Mobile():
   def __intit__(self,mbcolor,mbprice,mbversion,mbfeature,mbstorage,mbbatterycapacity):
      print("mobile object is created")
      self.Mbcolor=mbcolor
      self.Mbprice=mbprice
      self.Mbversion=mbversion
      self.Mbfeature=mbfeature
      self.Mbstorage=mbstorage
      self.Mbbatterycapacity=mbbatterycapacity
def display_items(self):
   print(f"the color of mobile is{self.Mbcolor}")
   print(f"the price of mobile:{self.Mbprice}")
   print(f"the versin of mobile :{self.Mbversion}")
   print(f"the feature of mobilr:{self.Mbfeature}")
   print(f"the storage of mobile :{ self.Mbstorage}")
   print(f"the mobile batterycapacity:{self.Mbbatterycapacity}")
M1=Mobile("samsung","75000","3.o","fr","340","220")
M2=Mobile("vivo","1400","t2x5g","fds","220","456")
M3=Mobile("apple","4500","rt4","sdfg","433","345")
M4=Mobile("oppo","3500","typro","34rfv","308","459")
display_items(M1)
display_items(M2)
display_items(M3)
display_items(M4)

      


   
   
