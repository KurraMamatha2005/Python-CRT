"""single linked list"""
#creating a class of node 
class Node:
    #constructor
    def __init__(self,data):#node contains data and reference
        self.data=data
        self.next=None#next is a built in function in python
#creating a class of linked list
class Singlell:
    def __init__(self):
        self.head=None#head is pointing to first element in the node of a list if head is None ll is empty
#so we created a singlell and node so we have to trversal(going through one node to another node)
#so i am creating  function called traversal in ll
    def traversal(self):
        if self.head is None:
            print("linked list is empty")
        else:
            a=self.head#i am creating a temp variable a to store head data as we are using while loop so head value will be changed
        while a is not None:
            print(a.data,end=" ")
            a=a.next
#insertion at begining
    def insertbeg(self,data):
        #we are creating a new node nb
        nb=Node(data)#to take  value we write data in paranthesis
        #we are pointing this next adress to head 
        nb.next=self.head
        self.head=nb  
     # Method to insert a new node at the end of the list
    def insert_end(self, data):
        new_node = Node(data)     # create a new node with the given data
        if not self.head:         # if list is empty
            self.head = new_node  # new node becomes the head
            return
        tmp = self.head           # start at the head
        while tmp.next:           # traverse until we find the last node
            tmp = tmp.next
        tmp.next = new_node       # last node's next points to new node
   
# to print the complete linked list we are using a function show same as traversal
"""   def show(self):
        temp = self.head
        while temp:
            temp=temp.next
        print("None")"""

N1=Node(5)#here first we have to create a node and then we have to call function
Sll=Singlell()
Sll.head=N1#it represent head in node 1 to connect it
N2=Node(10)
N1.next=N2
N3=Node(15)
N2.next=N3
N4=Node(20)
N3.next=N4
N5=Node(25)
N4.next=N5#here we are traversing through each node so we write .next and connect through each node
Sll.insertbeg(7)
Sll.insert_end(32)
Sll.traversal()


