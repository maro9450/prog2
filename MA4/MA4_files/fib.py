def fib_py(n):
    if n<= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))

print(fib_py(10))