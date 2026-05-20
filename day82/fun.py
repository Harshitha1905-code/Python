def myfunc():
    x=300
    print(x)
    
myfunc()

def myfunc():
    x=300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

x=300
def myfunc():
    print(x)

myfunc()
print(x)

x=300
def myfunc():
    x=200
    print(x)
myfunc()

print(x)

def myfunc():
    global x
    x=300
myfunc()
print(x)

def myfunc1():

    x="Jane"
    def myfunc2():
        nonlocal x
        x="John"
    myfunc2()  

    return x

print(myfunc1())

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)
