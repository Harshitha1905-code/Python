#Palindrome Checker Goutam says a number to Tanul. Tanul reverses it and checks if it equals the original: print ‘Palindrome’ if yes, 
# ‘Not a Palindrome’ if no. If the number is negative, print ‘Invalid Input’. EXAMPLE Input: 21212 Output: Palindrome
n=int(input())
if n < 0:
    print("Invalid Input")
else:
    original=n
    reverse=0
    while n > 0:
        digit=n%10 #gets the last digit
        reverse=reverse*10+digit #builds the reversed number
        n=n//10#removes the last digit from n
    if original==reverse:
        print("Palindrome")
    else:
        print("Not a Palindrome")        
        