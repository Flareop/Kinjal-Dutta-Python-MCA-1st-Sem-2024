x1, y1 = 1, 2
x2, y2 = 2, 4
x3, y3 = 3, 6
area= (x1 * (y2 - y3) + x2 * (y3 - y1)+ x3 * (y1 - y2)) / 2.0
if area == 0:
    print("the points are collinear.")
else:
    print("the points are not collinear.")