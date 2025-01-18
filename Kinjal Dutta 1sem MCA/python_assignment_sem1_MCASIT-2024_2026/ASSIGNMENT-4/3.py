def fibonacci_sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1 
    
    a, b = 0, 1
    total = a + b 

    for _ in range(3 , n + 1):
       next_term = a + b
       total += next_term
       a , b = b, next_term

    return total

num_terms = int(input("enter the number of terms for the fibonacci series : "))

if num_terms < 1:
    print("Please enter a positive integer.")
else:
    result = fibonacci_sum(num_terms)
    print(f"The sum of the first {num_terms} terms of the Fibonacci series is {result}.")