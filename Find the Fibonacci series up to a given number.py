def fibonacci(n):
    fib_series = [0, 1]
    while fib_series[-1] < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:-1]

print(fibonacci(50))