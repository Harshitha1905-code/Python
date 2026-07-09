def countdown(n):
    if n<0:
        print("Done!")
    else:
        print(n)
        countdown(n-1)
countdown(9)        

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))    

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))    

#sum of numbers
def sum_of_numbers(n):
    if n==0:
        return 0
    else:
        return n+sum_of_numbers(n-1)
print(sum_of_numbers(5))   

#factorial of numbers
def factorial_of_numbers(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_of_numbers(n-1)
print(factorial_of_numbers(5))  

#def hello():
   # print("Hi")
    #hello()

#hello()
#The function never stops calling itself, so Python eventually raises:RecursionError: maximum recursion depth exceeded

#print numbers from 1 to n
def print_numbers(n):
    if n==0:
        return
    else:
        print_numbers(n-1)
        print(n)
print_numbers(5)  

#Find the sum of the first n natural numbers.
#Calculate the factorial of n.
#Find the nth Fibonacci number.
#Reverse a string recursively.

def sum_of_natural_numbers(n):
    if n==0:
        return 0
    else:
        return n+sum_of_natural_numbers(n-1)
print(sum_of_natural_numbers(5))

#calculate the factorial of n.
def factorial_of_n(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_of_n(n-1)
print(factorial_of_n(5))

#Find the nth Fibonacci number.
def fibonacci_of_n(n):
    if n<=1:
        return n
    else:
        return fibonacci_of_n(n-1)+fibonacci_of_n(n-2)
print(fibonacci_of_n(7))

#Reverse a string recursively.
def reverse_string(s):
    if len(s)==0:
        return s
    else:
        return s[-1]+reverse_string(s[:-1])
print(reverse_string("hello"))

