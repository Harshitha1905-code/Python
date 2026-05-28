def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase
def myfunction():
    return "Hello Sally"
print(myfunction())

def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase
def myfunction():
    return "Hello Sally"
@changecase
def myfunction2():
    return "Hello John"
print(myfunction())
print(myfunction2())

def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

