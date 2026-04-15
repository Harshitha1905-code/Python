#reverse a string using functions
def reverse_string(s):
    return s[::-1]
n=input("Enter a string:")
reversed_n=reverse_string(n)
print("Reversed string:", reversed_n)