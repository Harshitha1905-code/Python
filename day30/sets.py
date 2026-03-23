set={"apple","banana","cherry"}
set.remove("banana")#If the item to remove does not exist, remove() will raise an error.
print(set)

set={"apple","banana","cherry"}
set.discard("banana")#If the item to remove does not exist, discard() will NOT raise an error.
print(set)


