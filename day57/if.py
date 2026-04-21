#and operator
a=200
b=33
c=500
if a > b and c > a:
  print("Both conditions are True")

#or operator
a=200
b=33
c=500
if a > b or a > c:
    print("At least one of the conditions is True")

#not operator
a=200
b=33
if not a > b:
    print("a is not greater than b")    


age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

score=89
if score<90 and score<=80:
       print("Grade: B")
else:
        print("Grade: A")    

username="admin"
password="1234"
if username=="admin" or password=="1234":
    print("Access granted")
else:  
     print("Access denied")
     
     