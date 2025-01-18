
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))


if a > b and a > c:
    longest = a
    side1, side2 = b, c
elif b > a and b > c:
    longest = b
    side1, side2 = a, c
else:
    longest = c
    side1, side2 = a, b


if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        print("The triangle is equilateral.")
    elif a == b or b == c or a == c:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
    
   
    if longest**2 == side1**2 + side2**2:
        print("The triangle is also a right-angled triangle.")
else:
    print("The entered sides do not form a valid triangle.")
