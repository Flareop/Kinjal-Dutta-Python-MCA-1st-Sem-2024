base = int(input("enter the base :"))
exponent = int(input("enter the exponent :"))

result = 1

for _ in range(exponent):
    result *= base

print(f"the value of {base} raised to the power of {exponent} is: {base}")
