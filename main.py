def area(base,height):
    return (base*height)/2
area_a=area(3,4)
area_b=area(4,5)
sum=area_a+area_b
print("area is ",str(sum))

# 2.......................................................function
def area_circle(radius):
    pi=3.14
    return (pi*(radius**2))
result=area_circle(4)
print("radies is" ,str(result))

#3
def conver_meter(km):
    m=1000
    return km*m
ans=conver_meter(6)
print(str(ans))

#4
def arr(list):
    list.sort()
    return list
ans=arr([9,8,6,2,3,1])
print(ans)

#4..........................................................string
string=("i am a python programmer")
print(string.split())
string= "".join(string)
print(string)

#5............................................dictionary
dict={
    "name":"ali",
    12:"age",
    "username":11223
}
dict["adress"]={
     "city": "Bahawalpur",
    "country": "Pakistan"
}
print(dict),
dict["name"]="ahmad"
dict["email"]="123@gmail.com"

print(dict)
dict.pop(12)
print(dict)
dict.popitem()
print(dict)
print(dict.keys())
print(dict.values())
print(len(dict))
if "name" in dict:
    print("exist")
print(dict["adress"])
dict["key"] = {
    "inner_key": "value"
}


#6 ...........................................................................................sets

value={2,2,5,5,7,8,2,9,36,8,"Ali",56,"python"}
print(value)

value.add("yes")
print(value)

value.remove("Ali")
print(value)

value.pop()
print(value)
value2={1,9,3,"Roman"}
print(value|value2)
print(value-value2)
print(value^value2)
print(value&value2)
value.clear()
print(value)
