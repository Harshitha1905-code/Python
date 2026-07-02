#add two numbers
def add_numbers(a, b):
    print("The sum of", a, "and", b, "is:", a + b)
sum1 = int(input("Enter first number: "))
sum2 = int(input("Enter second number: "))
add_numbers(sum1, sum2)    

#check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")  
num=int(input("Enter a number:"))  
check_even_odd(num)

#find maximum number
def find_maximum(a, b):
    if a > b:
        print(a, "is the maximum number.")
    elif b > a:
        print(b, "is the maximum number.")
    else:
        print("Both numbers are equal.")
max1 = int(input("Enter first number: "))
max2 = int(input("Enter second number: "))
find_maximum(max1, max2) 

#calculate factorial
def calculate_factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    elif n == 0:
        print("The factorial of 0 is 1.")
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        print("The factorial of", n, "is:", factorial)

n = int(input("Enter a number: "))
calculate_factorial(n)

#reverse a string
def reverse_string(s):
    reversed_str = s[::-1]
    print("The reversed string is:", reversed_str)

str = input("Enter a string: ")
reverse_string(str)
