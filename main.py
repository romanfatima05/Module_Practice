class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4=Node(40)
n1.next = n2
n2.next = n3
n3.next = n4

# Display the linked list
current = n1

while current is not  None:
    print(current.data, end=" -> ")
    current = current.next

print("None")



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4=Node(40)
n1.next = n2
n2.next = n3
n3.next = n4
new_node = Node(5)

# Insert at the beginning
new_node.next = n1
head = new_node

# Display the linked list
current = head

while current is not  None:
    print(current.data, end=" -> ")
    current = current.next

print("None")



class node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=node(10)
n2=node(13)
n3=node(45)
n1.next=n2
n2.next=n3

new_node=node(87)
current = n1

while current.next is not  None:
   
    current = current.next
current.next = new_node

# Display the list
current = n1
while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")


class node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=node(10)
n2=node(13)
n3=node(45)
n1.next=n2
n2.next=n3

# Display the list
target = 41
current = n1
found = False

while current is not None:
    if current.data==target:
        found =True
        break
   
    current = current.next

if found:
    print("Found")
else:
    print("Not found")

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=node(10)
n2=node(13)
n3=node(45)
n1.next=n2
n2.next=n3

# Display the list
target = 45
head= n1

if head is not None and head.data == target:
    head = head.next
else:
     current = head

while current is not None and current.next is not None:
        if current.next.data == target:
            current.next = current.next.next
            break

        current = current.next
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")






