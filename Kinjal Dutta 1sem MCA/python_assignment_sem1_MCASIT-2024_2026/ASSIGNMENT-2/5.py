num = int(input("enter numbers :" ))
a = num
sum = 0
while (num > 0):
    rem=num % 10
    sum=(sum*10)+rem
    num=num//10
if(a==sum):
    print("it is a reverse number")
else:
    print("it is not a reverse number")