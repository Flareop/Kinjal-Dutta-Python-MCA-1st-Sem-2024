def is_palindrome(number):
  
    str_number = str(number)
    return str_number == str_number[::-1]


num = int(input("Enter a number to check if it's a palindrome: "))


if is_palindrome(num):
    print(f"The number {num} is a palindrome.")
else:
    print(f"The number {num} is not a palindrome.")
