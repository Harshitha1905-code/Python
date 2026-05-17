#reverse a string
b = "hello"
print(b[::-1])

#finding maximum number in a list
list1 = [1, 2, 3, 4, 5]
max_num = max(list1)
print(max_num)

#finding even numbers in a list
list1 = [1, 2, 3, 4, 5, 6]
for num in list1:
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is not an even number")   

#finding prime numbers in a list
list1 = [1, 2, 3, 4, 5]
for num in list1:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")         

