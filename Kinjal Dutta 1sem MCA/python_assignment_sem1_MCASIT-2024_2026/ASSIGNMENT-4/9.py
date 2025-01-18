
def power(a, b):
    result = 1
    for _ in range(abs(b)): 
        result *= a
    if b < 0:  
        result = 1 / result
    return result


a = float(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))


result = power(a, b)
print(f"{a} raised to the power of {b} is: {result}")
