n=5
fac=1
for i in range(1,n+1):
    fac=fac*i
print(fac)
        
#......................................................


n = 81

for i in range(n + 1):
    if i * i == n:
        print(i)
        break

#..........................................................

n = 17
prime = True

if n <= 1:
    prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

if prime:
    print("Prime")
else:
    print("Not Prime")

#....................................................................

n = 12345
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print(rev)

#.....................................................................

a=25
b=35
while b != 0:
    remainder = a % b
    a = b
    b = remainder

print(a)
#.....................................................................
arr = [10, 5, 8, 20, 15]

largest = arr[0]
second = None

for i in range(1, len(arr)):
    if arr[i] > largest:
        second = largest
        largest = arr[i]
    elif second is None or arr[i] > second:
        second = arr[i]

print(second)
#..........................................................
n = 12345
sum = 0

while n > 0:
    digit = n % 10
    n = n // 10
    sum=sum+digit

print(sum)

#...............................................................
arr = [2, 4, 6, 8, 10]
target = 8

low = 0
high = len(arr) - 1
found = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        found = mid
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print(found)

#.......................................................
n = 7

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c

#.............................................................

arr = [3, 10, 2, 1, 20]

dp = [1] * len(arr)

for i in range(len(arr)):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print("\n",max(dp))