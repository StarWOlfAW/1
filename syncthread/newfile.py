import multiprocessing
import math
import time 
def f(x):
    return math.factorial(x)
t = multiprocessing.Process(target = f, args = [1000000])
t3 = multiprocessing.Process(target = f, args = [1000000])
if __name__ == "__main__":
    t1 = time.time()
    t.start()
    t3.start()
    t.join()
    t3.join()
    t2 = time.time()
    print(t2 - t1)