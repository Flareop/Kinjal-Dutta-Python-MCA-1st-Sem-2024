try:
    numbers = list(map(int, input("enter numbers separated by space: ").split()))

    if not numbers:
        print("the list is empty . Please enter valid numbers.")
    else:

        smallest = numbers[0]
        largest =  numbers[0]

        for num in numbers:
            if num < smallest:
                smallest = num
            if num > largest:
                largest = num

        range_of_numbers = largest - smallest

        print(f"the range of the set of numbers is : {range_of_numbers}")

except ValueError:
    print("please enter valid integer.")