num = int(input("enter the number to check the armstrong number: "))
sum =0 
temp = num

while num > 0 :
    digit = num % 10
    sum += digit ** 3
    num =num//10
    

if sum == temp:
    print("armstong.")
else:
    print("not armstong.")