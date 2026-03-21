#in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits=("apple","cherry","melon")
(green,yellow,blue)=fruits
print(green)
print(yellow)
print(blue)

#if no of variables is less than no of values in tuple you can add asterisk(*)
#to variable name and values will assign to variables as a list
fruits=("apple","cherry","melon","mango","strawberry")
(green,yellow,*blue)=fruits
print(green)
print(yellow)
print(blue)

fruits=("apple","cherry","melon","strawberry","orange","mango")
(green,*yellow,blue)=fruits
print(green)
print(yellow)
print(blue)

#loop through tuples
fruits=("apple","banana","cherry")
for x in fruits:
    print(x)

#loop through index numbers
fruits=("apple","banana","cherry")
for i in range(len(fruits)):
    print(fruits[i]) 

#using while loop
fruits=("apple","banana","cherry")
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1  

