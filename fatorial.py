def factorial(n: int):
    if (n == 0):  # base case
        return n
    if (n == 1):
        return 1
    return factorial(n-1) * n  # recursive case


print(factorial(4))
