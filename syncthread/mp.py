import multiprocessing
import math
import time
def f(x):
    return math.factorial(x)

if __name__ == "__main__":
    t1 = time.time()
    with multiprocessing.Pool(2) as p:
        p.map(f, [1000000, 200000])

    t2= time.time()
    print(t2 - t1)