def fibonacci(n):
    # write your code here
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


print(fibonacci(5))