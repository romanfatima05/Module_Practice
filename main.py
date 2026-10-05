#loop
i=1
sum=1

while i<=5:
    sum+=i
    i+=1
    #sum*=i
    print(sum)
#recursion    
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

n = int(input("Enter n: "))
print(sum_n(n))
#loop
i=1
fac=1
while i<=5:
    fac*=i
    i+=1
    
    print(fac)
#recursion
def fac_n(n):
    if n == 0:
        return 1
    return n * fac_n(n - 1)

n = int(input("Enter n: "))
print(fac_n(n))
#recursion
def fib(n):
    if(n==0):
        return 0
    if (n==1):
        return 1
    return fib(n-1)+fib(n-2)

n = int(input("Enter n: "))
print(fib(n))
def fib(n):
    if(n==0):
        return 0
    if (n==1):
        return 1
    return fib(n-1)+fib(n-2)
for i in range(5):
    print(fib(i), end=" ")