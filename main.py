arr0=[1,2,3,4,5,6,7]
for i in range(len(arr0)):
    print(arr0[i])
arr=[10,20,30,40,34]
value=67    

index=2
arr.append(0)
for i in range(len(arr)-1,index,-1):
    arr[i] = arr[i - 1]
arr[index] = value
print(arr)


arr2=[10,20,30,40,34]
index=2
for i in range(len(arr2)-1,index):
    arr2[i] = arr2[i + 1]
arr2[index] = value
print(arr2)

arr3=[12,13,14,16,17]
target=16
for i in range(len(arr3)):
    if arr3[i]==target:
        arr3[i]=24
print(arr3)

arr4=[10,83,92,29]
target=83
found=False
for i in arr4:
    if i==target:
        found=True
        break
if found:
    print("found",i)


even=[2,4,5,6,8,9,1]
count=0
for i in range(len(even)):
    if i%2==0:
        count+=1
print(count)

odd=[2,4,5,6,8,9,1]
count=0
for i in range(len(odd)):
    if i%2!=0:
        count+=1
print(count)

arr6=[3,9,18,40,1]
largest=arr6[0]
for i in range(len(arr6)):
    if arr6[i]>largest:
        largest=arr6[i]
print(largest)

#linkedlist program............................................................
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=node(10)
n2=node(20)
n3=node(40)
n1.next=n2
n2.next=n3
current=n1
while current is not None:
    print(current.data,end="->")
    current = current.next

print("None")

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=node(10)
n2=node(20)
n3=node(40)
n1.next=n2
n2.next=n3
current=n1
while current is not None:
    print(current.data,end="->")
    current = current.next

print("None")
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=node(10)
n2=node(20)
n3=node(40)
n1.next=n2
n2.next=n3
n4=node(50)
n3.next=n4
current=n1

while current is not None:
    print(current.data,end="->")
    current = current.next

print("None")

print("None")
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=node(10)
n2=node(20)
n3=node(40)
n1.next=n2
n2.next=n3
n4=node(50)
n3.next=n4

new_node=node(78)
new_node.next=n1
head=new_node
current=head
while current is not None:
    
    print(current.data,end="->")
    current = current.next

print("None")

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=node(10)
n2=node(20)
n3=node(40)
n1.next=n2
n2.next=n3
target=20
current=n1
found=False
while current is not None:
    if current.data==target:
        found=True
        break

    current = current.next
if found:
    print("found")
else:
    print("Not found")

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=node(10)
n2=node(20)
n3=node(40)
n1.next=n2
n2.next=n3
target=20
head=n1
if head is not None and head.data==target:
    head=head.next
else:
    current = head
    while current is not None and current.next is not None:
        if current.next.data == target:
            current.next = current.next.next
            break

        current = current.next

# Display the list
current = head

while current is not None:
    print(current.data,end="->")

    current = current.next
print("none")

#stack.............................................................................
stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# Pop the top element
remove=stack.pop()
print(remove)

print(stack)


stack1 = [10, 20, 30, 40]
remove=stack1.pop(-1)
print(remove)
print(stack1)


stack2 = [10, 20, 30, 40]
print(stack2[-1])

stack4 = [10, 20, 30, 40]
target = 30
found=False
for i in stack4:
    if i==target:
        found=True
        break
if found:
    print("found")
else:
    print("no")

stack9 = [1, 2, 3, 4]
reversed_stack = []

while stack9:
    item = stack9.pop()
    reversed_stack.append(item)

print(reversed_stack)