def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
num = int(input("enter a number to check if it's even or odd: "))

result = check_even_odd(num)
print(f"The number {num} is {result}.")