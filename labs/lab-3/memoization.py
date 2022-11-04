from timeit import Timer, timeit
from functools import lru_cache

# naive implementation of the Fibonacci function
def fib1(n) :
    if n<=1 :
        return n
    else :
        return fib1(n-1) + fib1(n-2)

# using a cache for the Fibonacci function
def fib2(n) :
    if n in cache :
        return cache[ n]
    if n<=1 :
        cache[ n] = n
        return n
    else :
        cache[ n] = fib2(n-1) + fib2(n-2)
        return cache[ n]


@lru_cache()                 
# using the caching system in Python for the Fibonacci function
def fib3(n) :
    if n<=1 :
        return n
    else :
        return fib3(n-1) + fib3(n-2)

# calls Fibonacci function
print(fib1(4))
cache = {}
print(type(cache))
print(fib2(4))
print(fib3(4))

t1 = Timer("fib1(15)", "from __main__ import fib1")
print("fib1 ",t1.timeit(number=1), "milliseconds")
t2 = Timer("fib2(15)", "from __main__ import fib2")
print("fib2 ",t2.timeit(number=1), "milliseconds")
t3 = Timer("fib3(15)", "from __main__ import fib3")
print("fib3 ",t3.timeit(number=1), "milliseconds")  