day=7
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")    
    case _:#default case
        print("Weekend")

day=4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case _:
        print("Weekend")    

month=5
day=4
match day:
    case 1|2|3|4|5 if month==5:
        print("It's May and it's a weekday.") 
    case 1|2|3|4|5:
        print("It's a weekday but not May.")   


month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
