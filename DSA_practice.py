
def fib_1(n):
   if (n==0):
      return 0
   if (n==1):
      return (1)
   return fib_1(n-1)+fib_1(n-2)
for i in range(13):
   print(fib_1(i))




def fac(n):
   if (n==0 or n==1):
      return 1
   return n*fac(n-1)
for i in range(6):
   print(fac(i))


word="madam"
rev=""
for i in range(len(word)-1,-1,-1):
   rev=rev+word[i]

if word == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

arr = [90, 200, 30, 80, 50, 40, 390]
target = 40
for i in range(len(arr)-1):
   for j in range(len(arr)-1 -i):
      if arr[j]>arr[j+1]:
         temp=arr[j]
         arr[j]=arr[j+1]
         arr[j+1]=temp
print("sorted list",arr)
low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Found at index", mid)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

def hanoi(n,source,auxillary,destination):
   if n==1:
      print(source,"->",destination)
      return
   hanoi(n-1,source,destination,auxillary)
   print(source,"->",destination)
   hanoi(n-1,auxillary,source,destination)
   
hanoi(3,"A", "B", "C")

#minmax...................
arr=[10,5,6,20,15]
min=arr[0]
max=arr[0]
for i in range(1,len(arr)):
   if arr[i]>max:
      max=arr[i]
   if arr[i]<min:
      min=arr[i]
print("Maximum:", max)
print("Minimum:", min)

arr = [10, 5, 8, 20, 15]

for i in range(len(arr)):
    largest = True

    for j in range(len(arr)):
        if arr[j] > arr[i]:
            largest = False
            break

    if largest:
        print("Maximum:", arr[i])
        break

#.....................................................merge sort
def merge_sort(arr):
   if len(arr)<=1:
      return arr
   mid=len(arr)//2
   left=merge_sort(arr[:mid])
   right=merge_sort(arr[mid:])

   result=[]
   i=0
   j=0
   while i < len(left) and j < len(right):
      if left[i]<=right[j]:
        result.append(left[i])
        i += 1
      else:
         result.append(right[j])
         j += 1
   result.extend(left[i:])
   result.extend(right[j:])
   return result
arr=[8,3,6,2,5,0,12]
print(merge_sort(arr))

#.................................heap min
import heapq
arr=[3,9,2,10]
heapq.heapify(arr)
print(arr)
print(heapq.heappop(arr))
removed=heapq.heappop(arr)
print(removed)
print(arr)
heapq.heappush(arr,12)
print(arr)
print("small",arr[0])


#................................................heap max

arr=[4,8,3,10,9]
max_heap=[-x for x in arr]
heapq.heapify(max_heap)
print(max_heap)
largest=-(heapq.heappop(max_heap))
print(largest)

#..............................................binary search
arr=[2,4,6,8,10,12]
target=10
low=arr[0]
high=len(arr)-1
while low<=high:
   mid=(low+high)//2
   if arr[mid]==target:
      print("found",mid)
      break
   if arr[mid]<target:
      low=mid+1
   else:
      high=mid-1

#.........................................................bubble sort
arr=[2,0,4,3,1]
for i in range(len(arr)):
   for j in range(len(arr)-1-i):
      if arr[j]>=arr[j+1]:
         temp=arr[j]
         arr[j]=arr[j+1]
         arr[j+1]=temp
print(arr)





   