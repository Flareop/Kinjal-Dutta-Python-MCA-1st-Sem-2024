try :
    num = int(input("enter a decimal number : "))
    if num == 0:
        print("the octal equvalent of 0 is : 0")
    else:
        is_negative = num < 0
        if is_negative:
            num = -num

        octal_number = ""
        while num > 0:
            remainder = num % 8
            octal_number = str(remainder) + octal_number
            num //= 8

        if is_negative :
            octal_number= "-" + octal_number

        print(f"the octal equvalent is : {octal_number}")
except ValueError:
    print("please enter a valid integer.")


