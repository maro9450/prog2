def fib_py(n):
    if n<= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))

from integer import Integer
import time
import matplotlib.pyplot as plt


def main():
    i=Integer(47)
    print(f"fib 47={i.start_fib()}")    
    N = [e for e in range(30,46)]
    times_py=[]
    times_c=[]
    for n in N:
        start = time.perf_counter()
        fib_py(n)
        stop = time.perf_counter()
        times_py.append(stop-start)

        start = time.perf_counter()
        f = Integer(n)
        f.start_fib()
        stop = time.perf_counter()
        times_c.append(stop-start)

    print(f"python times: {times_py}")
    print(f"C++ times: {times_c}")

    plt.plot(N,times_py,label='python')
    plt.plot(N,times_c,label='C++')
    plt.legend()
    plt.show
    plt.savefig(f"fib_times.png")


if __name__ == '__main__':
	main()