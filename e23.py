def fib(n):
    fib1 = 0
    fib2 = 1
    for i in range(n):
        fib1 = fib1 + fib2
        fib2 = fib1 - fib2
    return fib1

def f(n):
    if n == 21: return 1
    if n > 21:  return 0
    return f(n+1) + f(n+3) + f(fib(n))


print(f(6))