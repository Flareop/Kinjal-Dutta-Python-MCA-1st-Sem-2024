ram = float(input("enter age of ram :"))
shyam = float(input("enter age of shyam :"))
ajay = float(input("enter age of ajay :"))
if (ram < shyam and ram < ajay):
    print("Ram is youngest one ")
elif (shyam < ram and shyam < ajay):
    print("shyam is youngest one")
else:
    print("ajay is youngest one")
