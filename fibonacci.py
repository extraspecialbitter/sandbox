def fibonacci(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series[:n]

# Taking user input for the number of terms
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Checking if the input is valid
if n <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci(n)
    print(f"The first {n} numbers of the Fibonacci series are: {result}")

