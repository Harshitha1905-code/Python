def factorial(n):
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)        