def changecase(func):
    def myinner(x):
        return func(x).upper()
    return myinner
@changecase
def myfunction(nam):
    return "Hello "+nam
print(myfunction("sachin"))

def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner
@changecase
def myfunction(nam):
  return "Hello " + nam
print(myfunction("John"))

def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase
@changecase(1)
def myfunction():
  return "Hello Linus"
print(myfunction())
