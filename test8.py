#Buzz Number Check Check whether a number is a Buzz number. A Buzz number ends with the digit 7 or is divisible by 7.
#  (e.g. 42 divisible by 7; 107 ends with 7; 147 both.)
n=int(input())
if n % 7 == 0 or n % 10 == 7:#ends with digit 7 or divisible by 7
    print("Buzz Number")
else:
    print("Not a Buzz Number")