positive_count = 0
negative_count = 0
zero_count = 0

while True :
    num = int(input("enter the numner(end untill zero): "))
    if num == 0:
        zero_count +=1
        break
    elif num > 0:
        positive_count +=1
    else:
        negative_count +=1

    print("count the positive number", positive_count)
    print("count the negative number", negative_count)
    print("enter the zero", zero_count)
