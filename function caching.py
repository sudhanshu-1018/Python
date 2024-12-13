import functools
@functools.lru_cache(maxsize=None)
def fib(n):
    if n<2:
      return n
    return fib(n-1) + fib(n-2)
print(fib(20))


import time
from functools import lru_cache
@lru_cache(maxsize=None)
def fx(n):
   time.sleep(2)
   return n*5
print(fx(20))
print("done for 20")
print(fx(6))
print("done for 6")
print(fx(18))
print("done for 18")
print(fx(20))
print("done for 20")
print(fx(6))
print("done for 6")