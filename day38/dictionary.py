dict={
    "name":"Harshitha",
    "age":20,
    "year":1964
}
dict["year"]=2020
print(dict)

d={
    "name":"harshitha",
    "age":20,
    "year":2005
}
d.update({"name":"harshitha goud"})
print(d)

#pop method
dict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
dict.pop("model")
print(dict)

dict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
dict.pop("model")
print(dict)

d={
    "name":"harshitha",
    "age":20,
    "year":2005
}
d.popitem()
print(d)

d={
    "name":"harshitha",
    "age":20,
    "year":2005
}
del d["age"]
print(d)

dict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
dict.clear()
print(dict)

