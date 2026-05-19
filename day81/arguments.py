def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

def my_function(greeting, *names):
        for name in names:
             print(greeting,name)

my_function("Hello", "Emil", "Tobias", "Linus") 

def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(my_function(1, 2, 3, 4, 5))
print(my_function(10, 20, 30)) 

def my_function(*numbers):
     if len(numbers) == 0:
         return 0
     max_num = numbers[0]
     for num in numbers:
         if num > max_num:
             max_num = num
             return max_num
print(my_function(1, 2, 3, 4, 5))

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

def my_function(username, **details):
    print("Username:", username)
    for key, value in details.items():
        print(key + ":", value)
my_function("Tobias", age=30, city="Bergen", occupation="Developer")

def my_function(title,*args,**kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
my_function("My Title", "arg1", "arg2", key1="value1", key2="value2")

def my_function(a,b,c):
    return a + b + c
numbers=[1,2,3]
result=my_function(*numbers)
print(result)

def my_function(fname,lname):
    print("hello",fname,lname)
person={"fname":"John","lname":"Doe"}
my_function(**person)    
        