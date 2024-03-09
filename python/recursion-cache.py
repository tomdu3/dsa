cache = [None]*(100)

def fibonacci(n): 
    if n <= 1:
        return n

    # Check if the value exists
    if not cache[n]:

        # Save the result in cache
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]


print(fibonacci(6))
