
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



   