my_dict={
    "Harshitha":100,
    "Sravani":90,
    "Akhilesh":80,
}
print(my_dict.keys())
print(my_dict.values())

#Add a new key-value pair to the dictionary
my_dict["Geetha"] = 95
print(my_dict)

#Remove a key "age" from a dictionary:
d={
    "name":"Harshitha",
    "age":20,
    "city":"Hyderabad"
}
#d.pop("age")
del d["age"]
print(d)

#Check if a key "salary" exists in a dictionary.
dict={
    "name":"Harsh",
    "age":20,
    "salary":50000
}
if "salary" in dict:
    print("Key 'salary' exists in the dictionary.")

#Count how many key-value pairs are in a dictionary.
my_dict={
    "Harshitha":100,
    "Sravani":90,
    "Akhilesh":80,
}
print(len(my_dict)) 

