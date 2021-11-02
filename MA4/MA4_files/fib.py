def fib_py(n):
    if n<= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))

from integer import Integer


def main():
    n = 30
    f = Integer(n)
    print(f.start_fib())

    print(fib_py(n))


if __name__ == '__main__':
	main()