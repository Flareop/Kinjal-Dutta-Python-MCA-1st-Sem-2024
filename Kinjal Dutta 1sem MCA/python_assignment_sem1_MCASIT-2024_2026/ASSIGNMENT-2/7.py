s1 = int(input("enter the triangle side-1 :"))
s2 = int(input("enter the triangle side-2 :"))
s3 = int(input("enter the triangle side-3 :"))
sum=s1+s2+s3
if(sum==180):
    print("Valid Triangle")
else:
    print("Not Valid ")