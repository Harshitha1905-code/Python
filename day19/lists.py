#PYTHON ADD LIST ITEMS
#Append items
thislist=["Apple","Banana","kiwi"]
thislist.append("mango")
print(thislist)

#insert method
list=["Apple","Banana","kiwi"]
list.insert(2,"mango")
print(list)

#extend method-The elements will be added to the end of the list.
thislist=["Apple","Banana","orange"]
tropical=["mango","kiwi","grapes"]
thislist.extend(tropical)
print(thislist)

#python remove items
thislist=['apple','banana','kiwi']
thislist.remove("apple")
print(thislist)

#If there are more than one item with the specified value, the remove() method removes the first occurrence:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#to remove specified index we use pop method
thislist=["apple","banana","cherry"]
thislist.pop(2)
print(thislist)