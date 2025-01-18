year = int(input("enter year:"))
days = (year - 1900) * 365 + ( year - 1900)
days_of_weeks = days % 7
if days_of_weeks == 0:
    print("Monday")
elif days_of_weeks ==1:
    print("Tuesday")
elif days_of_weeks ==2:
    print("Wednesday")
elif days_of_weeks == 3:
    print("Thusday")
elif days_of_weeks == 4:
    print("Friday")
elif days_of_weeks == 5:
    print("Saturday")
else:
    print("Sunday")
