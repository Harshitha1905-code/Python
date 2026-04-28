fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)   

fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x=="banana":
        break

fruits=["apple","banana","cherry"]
for x in fruits:
    if x=="banana":
        break
        print(x)     


fruits=["apple","banana","cherry"]
for x in fruits:
    if x=="banana":
        continue
    print(x)    
      
for x in range(6):
    print(x)


for x in range(2,6):
    print(x) 

for x in range(2,30,3):
    print(x)

for x in range(6):
    print(x)    
else:
    print("Finally finished!")   

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")  


adj=["red","big","tasty"]
fruits=["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y) 

for x in [0,1,2]:
    pass     

#remove duplicates from list using functions
def remove_duplicates(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst
my_list = [1, 2, 3, 2, 4, 1, 5]
result = remove_duplicates(my_list)
print(result)
