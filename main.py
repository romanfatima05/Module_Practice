arr=[2,7,8,87]
index=2
value=43
arr.append(0)
for i in range(len(arr) - 1, index, -1):
    arr[i] = arr[i - 1]

arr[index] = value

print(arr)



arr=[10,20,30,40,50,60,70]
index=3
for i in range(index,(len(arr)-1)):
    arr[i]=arr[i + 1]
del arr[-1]
print(arr)

arr = [10, 20, 30, 40, 50, 60, 70]
target = 50

index = -1

# Find the target value
for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break

# Delete it if found
if index != -1:
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]

    del arr[-1]

print(arr)
               