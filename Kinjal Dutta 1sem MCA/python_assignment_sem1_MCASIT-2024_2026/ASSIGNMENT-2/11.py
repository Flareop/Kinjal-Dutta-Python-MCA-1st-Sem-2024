import math

# Input the center coordinates and radius of the circle
x_c = float(input("Enter the x-coordinate of the circle's center: "))
y_c = float(input("Enter the y-coordinate of the circle's center: "))
radius = float(input("Enter the radius of the circle: "))

# Input the coordinates of the point to check
x_p = float(input("Enter the x-coordinate of the point: "))
y_p = float(input("Enter the y-coordinate of the point: "))

# Calculate the distance between the center of the circle and the point
distance = math.sqrt(math.pow(x_p - x_c, 2) + math.pow(y_p - y_c, 2))

# Determine the position of the point relative to the circle
if distance < radius:
    print("The point lies inside the circle.")
elif distance == radius:
    print("The point lies on the circle.")
else:
    print("The point lies outside the circle.")
