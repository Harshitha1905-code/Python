set={"apple","banana","cherry"}
print(set)

s={"apple", "banana", "cherry", "apple"}
print(s)

#true and 1 are considered as same value in sets
set={"apple","banana","cherry",True,2,1}
print(set)

#false and 0 are considered as same values
set={"apple","banana","orange",True,False,0}
print(set)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

myset={"apple","banana","cherry"}
print(type(myset))

#thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
#print(thisset)

thisset={"apple","banana","cherry"}
for x in thisset:
    print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) 

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

