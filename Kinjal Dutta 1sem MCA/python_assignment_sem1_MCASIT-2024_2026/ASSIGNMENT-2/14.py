days = float(input("enter the number of days : "))
if (days > 0 and days <= 5 ):
    amt = 0.05
    print("fine amount pay Rs : ", amt)
elif (days >= 6 and days <=10 ):
    amt = 1
    print("fine amount pay Rs :",amt)
elif(days >= 11):
    amt = 5
    print("fine amount pay Rs : ", amt)
    if(days > 30):
        print("your membership will cancle")
else:
    ("not valid")
