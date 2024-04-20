import threading
import math
import time 
def f(x):
    return math.factorial(x)
t = threading.Thread(target = f, args = [1000000])
t3 = threading.Thread(target = f, args = [1000000])
t1 = time.time()
t.start()
t3.start()
t.join()
t3.join()
t2 = time.time()
print(t2 - t1)