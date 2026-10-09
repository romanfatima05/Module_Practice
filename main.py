arr=[2,9,6,8,45,90]
largest=arr[0]
for num in arr:
    if num > largest:
        largest=num
print(largest)


arr=[2,9,-6,8,45,90]
smallest=arr[0]
for num in arr:
    if num < smallest:
        smallest=num
print(smallest)


arr=[2,9,6,8]
total=0
for i in arr:
    total+=i
print(total)

arr=[2,9,7,8,4,3]
#result=arr[0]
for num in arr:
    if num %2==0:
        (print(num))

arr=[2,9,7,8,4,3]
result=0
for num in arr:
    if num %2==0:
        
        result+=1
print(result)


arr=[2,9,7,8,4,3]
result=0
for num in arr:
    if num %2!=0:
        
        result+=1
print(result)

arr=[10,25,30,46,50]
target=30
for i in arr:
    if i==target:
        print("found",i)
        break
else:
    print("not found")

arr=[10,25,30,46,50]
target=30
for i in range (len(arr)):
    if arr[i]==target:
        print("found",i)
        break
else:
    print("not found")

arr = [10, 25, 30, 46, 50]
target = 100
for i in range (len(arr)):
    if arr[i]==target:
        print("found",i)
        break
else:
    print("not found")

arr = [2, 5, 2, 8, 2, 9]
target = 2
count=0
for i in arr:
    if i==target:
        count+=1
print(count)

arr=[1,6,23.,56,78,50]
re=[]
for i in range ((len(arr))-1,-1,-1):
    
    re.append (arr[i])
print(re)

arr = [10, 20, 30, 20, 40, 10, 50]

seen = []
duplicates = []

for i in arr:
    if i in seen:
        if i not in duplicates:
            duplicates.append(i)
    else:
        seen.append(i)

print(duplicates)