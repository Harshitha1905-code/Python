if 7 > 10:
    print("7 is greater than 10")
else:
    print("7 is not greater than 10")


print(bool(0))#false
print(bool(1))#true
print(bool(-1))#true
print(bool(""))#false
print(bool("Hello"))#true

num=8
print(num>10)

print(5==5)
print(5==6)

#check if a number is even using booleans
num=4
print(num%2==0)

print(10 > 5 > 3)

x =" i am eating apple"
print("apple" in x) #true
print("banana" in x) #false

#difference between "is" and "=="
a = 7
b = 8
print(a == b) #=compares values
print(a is b) #compares identities (memory locations)

#can a boolean added to an integer?
print(True + 1) #True is treated as 1
print(False + 1) #False is treated as 0

