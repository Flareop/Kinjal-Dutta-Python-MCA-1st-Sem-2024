num = int(input("enter the number :"))
sum = 0

n = num //1000
sum = sum + n

n = num % 10
sum = sum + n
print("enter sum of the number :", sum)