# print 1 to n numbers sum using functions-recursion
def sum_of_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_numbers(n - 1)
n = int(input("Enter a number: "))
result = sum_of_numbers(n)
print("The sum of numbers from 1 to n is:", result)