class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
First=Node(10)
Second=Node(20)
Third=Node(30)
Fourth=Node(40)
Fifth=Node(50)          
head=First
head.next=Second
Second.next=Third 
Fourth.next=Fifth 
current=head
while current:
    print(current.data,end="-->")
    current=current.next
print("None")

###############
class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class Linklist():
    def __init__(self):
        self.head=None
    def add_node(self,data):
        n_node=Node(data)
        n_node.next=self.head
        self.head=n_node
N1=Node(25)
N2=Node(99.56)
N3=Node(76.54)
N4=Node(175.54)
current=N1
node=Node(10)
print(node.data)
node1=Node(20)
print(node.data)
node2=Node(30)
print(node2.data)
current=node
node.next=node1
node1.next=node2
while current:
    print(current.data, end=" -->")
    current=current.next
print("none")

#################
class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class Linklist():
    def __init__(self):
        self.head=None
    def add_node(self,data):
        n_node=Node(data)
        n_node.next=self.head
        self.head=n_node
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
    #count total number of nodes
    def count_nodes(self):
        count=0
        temp=self.head
        while temp:
          count+=1
          temp=temp.next
        return count
    def Display_list(self):
        current=self.head
        while current:
            print(current.data,end="-->")
            current=current.next
        print("None")
L1=Linklist()
L1.add_node(25.98)
L1.add_node(99.56)
L1.add_node(76.55)
L1.add_node(100)
L1.count_nodes()
L1.Display_list()

#manually create  linked list with 3 elements
a=Node(10)
b=Node(20)
c=Node(30)
a.next=b
b.next=c
temp =a
while temp:
    print(temp.data,end="-->")
    temp=temp.next
#count total number of nodes
def count_nodes(self):
    count=0
    temp=self.head
    while temp:
        count+=1
        temp=temp.next
    return count




