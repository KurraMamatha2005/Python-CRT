class Stack:
    def __init__(self):
        self.Stack=[]
    def push(self,data):
        self.Stack.append(data)
        print(f"{data} element is appended")
    def isempty(self):
        if len(self.Stack)==0:
            return True
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            self.Stack.pop()
            print("element is deleted")
    def display(self):
        for i in self.stack:
            print(i)

stack=Stack()
stack.push(100)
stack.push(105)
stack.push(106)
stack.push(107)



        