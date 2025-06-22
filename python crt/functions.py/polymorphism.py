#duck typing
class Duck:
    def walk(self):
        print("chapak chapak chapak")
class Horse:
    def walk(self):
        print("tapak tapak tapak")
def myfunction(obj):
    obj.walk()
d = Duck()
myfunction(d)
h=Horse()
myfunction(h)