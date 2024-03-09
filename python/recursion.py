def fibonacci(n):
    # Define the base case
    if n <= 1:
        return n
    else:
        # Call recursively to fibonacci
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6))
