#Swap two variables without using a third variable.
a = 5
b = 10
a, b = b, a
print("a:", a)
print("b:", b)

a=5
b=10
a = a + b
b = a - b
a = a - b
print("a:", a)
print("b:", b)

num=5
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")  

s="hello world"
count=0
for char in s:
    if char in ('a', 'e', 'i', 'o', 'u'):
        count += 1
print("Number of vowels in the string:", count)

a=12
b=15
c=9
if a > b and a > c:
    print(a, "is the largest number")
elif b > a and b > c:
    print(b, "is the largest number")
else:
    print(c, "is the largest number")    

  
 
