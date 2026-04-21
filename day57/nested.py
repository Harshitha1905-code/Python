x=41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

age=25
has_license=True
if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("You need a license to drive.")
else:
         print("You are too young to drive.") 


username="email"
password="python123"       
is_active=True
if username:
     if password:
        if is_active:
                print("Login successful!")
        else:
                print("Account is not active.")
     else:
            print("Password cannot be empty.")
else:
        print("Username cannot be empty.")

        
               