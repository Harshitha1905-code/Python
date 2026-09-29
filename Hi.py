#add 10 to argument a and return the result
x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))

x = lambda a,b,c: a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n
mydouble = myfunc(3)
print(mydouble(11))

def myfunc(n):
  return lambda a : a * n
mytriple = myfunc(5)
mydouble = myfunc(2)
print(mytriple(11))
print(mydouble(11))

numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#sort a list of tuples based on the second element
students = [('John', 25), ('Alice', 22), ('Bob', 30)]
sorted_students=sorted(students,key=lambda x: x[1])
print(sorted_students)

#sort strings by length
words = ['apple', 'banana', 'kiwi', 'grape']
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
