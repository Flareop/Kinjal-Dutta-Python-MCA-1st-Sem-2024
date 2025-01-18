
for i in range(10):
    print(f"Set {i + 1}:")
  
    p = float(input("Enter the principal amount (p): "))
    r = float(input("Enter the annual interest rate in percentage (r): ")) / 100  
    n = int(input("Enter the number of years (n): "))
    q = int(input("Enter the number of times interest compounds per year (q): "))

   
    a = p * (1 + r / q) ** (n * q)

    print(f"The compounded amount (a) is: {a:.2f}")
    print("-" * 30)
