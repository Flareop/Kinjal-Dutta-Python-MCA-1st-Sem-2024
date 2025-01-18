
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


def combinations(n, r):
    if r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))


n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))


result = combinations(n, r)
print(f"C({n}, {r}) = {result}")
