def factorial(n: int):
    if (n == 0):
        return n
    if (n == 1):
        return 1
    return factorial(n-1) * n


print(factorial(4))
