def my_function(fname,lname):
    print(fname + " " + lname)

my_function("Emil","Refsnes")

def my_function(name="freind"):
    print("Hello", name)

my_function("Emil")
my_function()
my_function("Tobias")

def my_function(animal,name):
    print('I have a',animal)
    print('My',animal + " s name is " + name)

my_function(animal="dog",name="Rexy") 

def my_function(animal,name):
    print('I have a',animal)
    print('My',animal + " s name is " + name)
my_function("dog","Rexy")    

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

def my_function(x,y):
    return x + y
result = my_function(5, 3)
print(result)

def my_function():
   return ['apple', 'banana', 'cherry']
fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)