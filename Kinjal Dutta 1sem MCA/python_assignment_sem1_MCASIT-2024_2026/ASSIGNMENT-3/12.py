n_term = 7
series_sum = 0

for n in range(1, n_term + 1):
    factorial = 1
    for i in range(1 , n + 1):
        factorial *= i

    term = n / factorial

    series_sum += term


print(f"the sum of the first {n_term} terms of the series is : { series_sum}")