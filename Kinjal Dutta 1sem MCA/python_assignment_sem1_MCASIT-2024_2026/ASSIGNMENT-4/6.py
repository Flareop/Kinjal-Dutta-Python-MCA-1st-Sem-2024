def sum_positive_negative(numbers):
    
    sum_positive = 0
    sum_negative = 0

    for num in numbers:
        if num > 0:
            sum_positive += num
        elif num < 0:
            sum_negative += num

    return sum_positive, sum_negative


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))


positive_sum, negative_sum = sum_positive_negative(numbers)


print(f"Sum of positive numbers: {positive_sum}")
print(f"Sum of negative numbers: {negative_sum}")
