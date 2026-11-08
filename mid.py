#factorial

def fac(n):
    if n==1:
        return n
    return n*fac(n-1)
factorial=fac(5)
print("fac :",factorial)

#fabnocciseries

def fab(n):
    if n==0:
        return 0
    if n==1:
            return 1
    return fab(n-1)+fab(n-2)
fabnacci=fab(8)
print("fabnacci :",fabnacci)


#Binary search

arr=[2,4,6,8,9,10]
Target=8
low=0
high=len(arr)-1
found=-1
while low<=high:
     mid=(low+high)//2
     if(arr[mid]==Target):
         found=mid
         break
     elif arr[mid]<Target:
       
          low=mid+1
     else:
          high=mid-1
print("binary :",found)

#Tower of Hanoi

def hanoi(n,source,auxillary,destination):
    if n==1:
        print(source,"->",destination)
        return
    hanoi(n-1,source,destination,auxillary)
    print(source,"->",destination)
    hanoi(n-1,auxillary,source,destination)
hanoi(3,"A", "B", "C")


#sorted 

arr1=[9,0,5,8,2,17,4]
for i in range(len(arr1)):
     for j in range(len(arr1)-1-i):
          if arr1[j]>=arr1[j+1]:
               temp=arr1[j]
               arr1[j]=arr1[j+1]
               arr1[j+1]=temp
print("sorted :",arr1)

#linear search
arr2=[2,6,7,8,9]
target=7
found=-1
for i in range(len(arr2)):
     if arr2[i]==target:
          found=i
          break
print("found linear :",found)

#first occurance
arr = [2, 5, 3, 5, 8, 5, 9]
target = 5
found = -1

for i in range(len(arr)):
    if arr[i] == target:
        found = i
        break

print("First occurrence:", found)

#last occurance
arr = [2, 5, 3, 5, 8, 5, 9]
target = 5
found = -1

for i in range(len(arr)):
    if arr[i] == target:
        found = i
        

print("last occurrence:", found)


#count 
arr = [2, 5, 3, 5, 8, 5, 9,5]
target = 5
count = 0

for i in range(len(arr)):
    if arr[i] == target:
        count += 1

print("count",count)

#all occurance
arr = [2, 5, 3, 5, 8, 5, 9]
target = 5

for i in range(len(arr)):
    if arr[i] == target:
        print("all occurance", i)

#selection sort
arr=[9,5,7,2,4]
for i in range(len(arr)):
    min=i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[min]:
             min=j
    temp = arr[i]
    arr[i] = arr[min]
    arr[min] = temp

print("selection sort",arr)

#insertionsort
arr = [7, 4, 5, 2, 6]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print(arr)

#merge sort
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [8, 3, 6, 2, 7, 1, 5]

print("merge_sort",merge_sort(arr))

#...quick sort
def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [8, 3, 6, 2, 7, 1, 5]

print(quick_sort(arr))

#linked list
class Node:
    def __init__(self,data):
       self.data=data
       self.next=None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.next=node2
node2.next=node3

current=node1
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# insert first

class Node:
    def __init__(self,data):
       self.data=data
       self.next=None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

new_node=Node(50)
new_node.next=node1
node1.next=node2
node2.next=node3
current=new_node
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# insert at end

class Node:
    def __init__(self,data):
       self.data=data
       self.next=None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
new_node=Node(40)
node1.next=node2
node2.next=node3
node3.next=new_node


current=node1
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# serach
class Node:
    def __init__(self,data):
       self.data=data
       self.next=None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.next = node2
node2.next = node3
target=30
current=node1
found=False
while current:
    if current.data==target:
        found=True
        break
    current = current.next
if found:
    print("found")
else:
    print("Element not found")

#delete
class Node:
    def __init__(self,data):
       self.data=data
       self.next=None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.next = node2
node2.next = node3
target=30
current=node1
while current and current.next:
    if current.next.data==target:
        current.next=current.next.next
        break
    current=current.next
current = node1
while current:
    print(current.data, end=" -> ")
    current = current.next

print("none")
#reverse
class Node:
    def __init__(self,data):
       self.data=data
       self.next=None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node3.next=node2
node2.next=node1

current=node3
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

#reverseee2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

prev = None
current = node1

while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node

# Print reversed linked list
current = prev

while current:
    print(current.data, end=" -> ")
    current = current.next
print("none")
#count

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

count = 0
current = node1

while current:
    count += 1
    current = current.next

print("Total nodes:", count)